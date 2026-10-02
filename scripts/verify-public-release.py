"""Read every public release asset without authentication and verify its bytes."""

import hashlib
import json
from pathlib import Path
import sys
import urllib.request

release = json.loads(Path(sys.argv[1]).read_text())["release"]
assert not release["draft"] and not release["prerelease"]
assets = {asset["name"]: asset for asset in release["assets"]}
assert "SHA256SUMS" in assets


def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "TopxAI-release-verification"}), timeout=120)


with fetch(assets["SHA256SUMS"]["browser_download_url"]) as response:
    checksums = response.read().decode()
expected = {}
for line in checksums.splitlines():
    sha256, name = line.split("  ", 1)
    assert len(sha256) == 64 and name not in expected
    expected[name] = sha256
assert set(expected) == set(assets) - {"SHA256SUMS"}
for name, asset in assets.items():
    digest = hashlib.sha256()
    size = 0
    with fetch(asset["browser_download_url"]) as response:
        while block := response.read(4 * 1024 * 1024):
            digest.update(block)
            size += len(block)
    assert size == asset["size"], name
    if name in expected:
        assert digest.hexdigest() == expected[name], name
    assert asset["digest"] == "sha256:" + digest.hexdigest(), name
    print(json.dumps({"name": name, "bytes": size, "sha256": digest.hexdigest(), "anonymousReadbackPassed": True}), flush=True)
print("All public assets verified end to end", flush=True)
