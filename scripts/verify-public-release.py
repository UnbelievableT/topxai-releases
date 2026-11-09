"""Read every public release asset anonymously and verify its complete bytes."""

import hashlib
import http.client
import json
from pathlib import Path
import re
import sys
import socket
import time
import urllib.error
import urllib.request

ATTEMPTS = 5
CHUNK_BYTES = 4 * 1024 * 1024


def read_asset(asset, collect=False, opener=urllib.request.urlopen, sleep=time.sleep):
    """Restart transiently interrupted streams so a retry cannot reuse partial hashes."""
    for attempt in range(ATTEMPTS):
        digest = hashlib.sha256()
        size = 0
        chunks = []
        try:
            request = urllib.request.Request(
                asset["browser_download_url"],
                headers={"User-Agent": "TopxAI-release-verification"},
            )
            with opener(request, timeout=120) as response:
                while block := response.read(CHUNK_BYTES):
                    digest.update(block)
                    size += len(block)
                    if collect:
                        if size > CHUNK_BYTES:
                            raise ValueError("SHA256SUMS exceeds 4 MiB")
                        chunks.append(block)
            if size != asset["size"]:
                raise http.client.IncompleteRead(b"", asset["size"] - size)
        except urllib.error.HTTPError as error:
            retry = error.code == 429 or 500 <= error.code < 600
            retry_after = error.headers.get("Retry-After", "") if error.headers else ""
            error.close()
            if not retry or attempt + 1 == ATTEMPTS:
                raise
            delay = min(60, int(retry_after)) if retry_after.isdigit() else 2 ** attempt
        except (urllib.error.URLError, TimeoutError, socket.timeout, ConnectionError, http.client.IncompleteRead):
            if attempt + 1 == ATTEMPTS:
                raise
            delay = 2 ** attempt
        else:
            sha256 = digest.hexdigest()
            if asset.get("digest") != "sha256:" + sha256:
                raise ValueError(f"GitHub digest mismatch: {asset['name']}")
            return {"name": asset["name"], "bytes": size, "sha256": sha256}, b"".join(chunks)
        print(f"Retrying {asset['name']} ({attempt + 2}/{ATTEMPTS}) after {delay}s", file=sys.stderr, flush=True)
        sleep(delay)
    raise RuntimeError("Unreachable retry state")


def verify(release):
    if release["draft"] or release["prerelease"]:
        raise ValueError("Expected a published stable release")
    assets = {asset["name"]: asset for asset in release["assets"]}
    if len(assets) != len(release["assets"]) or "SHA256SUMS" not in assets:
        raise ValueError("Duplicate assets or missing SHA256SUMS")
    sums_result, checksums = read_asset(assets["SHA256SUMS"], collect=True)
    expected = {}
    for line in checksums.decode().splitlines():
        sha256, name = line.split("  ", 1)
        if not re.fullmatch(r"[a-f0-9]{64}", sha256) or name in expected:
            raise ValueError("Invalid or duplicate SHA256SUMS entry")
        expected[name] = sha256
    if set(expected) != set(assets) - {"SHA256SUMS"}:
        raise ValueError("SHA256SUMS does not match the release's complete asset list")
    for name, asset in assets.items():
        result = sums_result if name == "SHA256SUMS" else read_asset(asset)[0]
        if name in expected and result["sha256"] != expected[name]:
            raise ValueError(f"SHA256SUMS mismatch: {name}")
        print(json.dumps({**result, "anonymousReadbackPassed": True}), flush=True)
    print("All public assets verified end to end", flush=True)


if __name__ == "__main__":
    verify(json.loads(Path(sys.argv[1]).read_text())["release"])
