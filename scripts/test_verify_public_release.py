import hashlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import Mock
import urllib.error

spec = importlib.util.spec_from_file_location('verify_public_release', Path(__file__).with_name('verify-public-release.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class BrokenStream(io.BytesIO):
    def read(self, size=-1):
        if self.tell():
            raise TimeoutError('read stalled')
        return super().read(2)


class ReadbackTests(unittest.TestCase):
    def asset(self, content=b'payload'):
        return dict(name='app.zip', size=len(content), digest='sha256:' + hashlib.sha256(content).hexdigest(), browser_download_url='https://example.invalid/app.zip')

    def test_restarts_hash_after_midstream_timeout(self):
        opener = Mock(side_effect=[BrokenStream(b'payload'), io.BytesIO(b'payload')])
        sleep = Mock()
        result, content = module.read_asset(self.asset(), collect=True, opener=opener, sleep=sleep)
        self.assertEqual(content, b'payload')
        self.assertEqual(result['bytes'], 7)
        self.assertEqual(opener.call_count, 2)
        sleep.assert_called_once_with(1)

    def test_retries_503_and_short_response(self):
        opener = Mock(side_effect=[urllib.error.HTTPError('url', 503, 'unavailable', {'Retry-After': '200'}, io.BytesIO()), io.BytesIO(b'pay'), io.BytesIO(b'payload')])
        sleep = Mock()
        module.read_asset(self.asset(), opener=opener, sleep=sleep)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [60, 2])

    def test_404_and_hash_mismatch_fail_without_retry(self):
        for response in [urllib.error.HTTPError('url', 404, 'missing', {}, io.BytesIO()), io.BytesIO(b'corrupt')]:
            opener = Mock(side_effect=[response])
            with self.assertRaises((urllib.error.HTTPError, ValueError)):
                module.read_asset(self.asset(), opener=opener, sleep=Mock())
            self.assertEqual(opener.call_count, 1)

    def test_exhaustion_never_reports_success(self):
        opener = Mock(side_effect=TimeoutError('stalled'))
        with self.assertRaises(TimeoutError):
            module.read_asset(self.asset(), opener=opener, sleep=Mock())
        self.assertEqual(opener.call_count, 5)


if __name__ == '__main__':
    unittest.main()
