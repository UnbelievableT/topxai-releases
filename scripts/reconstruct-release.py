"""Reconstruct a signed app from an authenticated, hash-checked release delta."""

import bz2
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tarfile


def digest(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def relative(value):
    path = Path(value)
    assert not path.is_absolute() and ".." not in path.parts
    return path


def integer(data):
    assert len(data) == 8
    value = int.from_bytes(data, "little")
    return -(value & ((1 << 63) - 1)) if value & (1 << 63) else value


def patch(old, delta):
    assert delta[:8] == b"BSDIFF40"
    control_len, diff_len, size = (integer(delta[p:p + 8]) for p in (8, 16, 24))
    assert 0 <= size < 1_000_000_000 and control_len >= 0 and diff_len >= 0
    controls = bz2.decompress(delta[32:32 + control_len])
    diffs = bz2.decompress(delta[32 + control_len:32 + control_len + diff_len])
    extra = bz2.decompress(delta[32 + control_len + diff_len:])
    out = bytearray(size)
    oldpos = newpos = diffpos = extrap = controlpos = 0
    while newpos < size:
        x, y, z = (integer(controls[p:p + 8]) for p in range(controlpos, controlpos + 24, 8))
        controlpos += 24
        assert x >= 0 and y >= 0 and newpos + x + y <= size
        assert diffpos + x <= len(diffs) and extrap + y <= len(extra)
        for offset in range(0, x, 65536):
            length = min(65536, x - offset)
            difference = diffs[diffpos + offset:diffpos + offset + length]
            position = oldpos + offset
            if 0 <= position and position + length <= len(old):
                basis = old[position:position + length]
            else:
                basis = bytes(old[p] if 0 <= p < len(old) else 0 for p in range(position, position + length))
            block = basis if difference.count(0) == length else bytes((a + b) & 255 for a, b in zip(basis, difference))
            out[newpos + offset:newpos + offset + length] = block
        newpos += x
        oldpos += x
        diffpos += x
        out[newpos:newpos + y] = extra[extrap:extrap + y]
        newpos += y
        extrap += y
        oldpos += z
    return out


def verify(app, entries):
    expected = set()
    for row in entries:
        path = app / relative(row["path"])
        expected.add(row["path"])
        if row["kind"] == "symlink":
            assert path.is_symlink() and os.readlink(path) == row["target"], row["path"]
        elif row["kind"] == "directory":
            assert path.is_dir() and not path.is_symlink(), row["path"]
        else:
            assert path.is_file() and not path.is_symlink(), row["path"]
            assert digest(path) == row["sha256"], row["path"]
            assert path.stat().st_mode & 0o777 == row["mode"], row["path"]
    actual = set()
    for directory, directories, files in os.walk(app, followlinks=False):
        for name in directories + files:
            actual.add(str((Path(directory) / name).relative_to(app)))
    assert actual == expected, "Unexpected app files"


if sys.argv[1] == "verify":
    manifest = json.loads(Path(sys.argv[3]).read_text())
    verify(Path(sys.argv[2]), manifest["entries"])
    print("Every mounted app file, symlink and mode verified")
    sys.exit(0)

bundle, basis, stage = map(Path, sys.argv[1:4])
assert digest(bundle) == os.environ["DELTA_SHA256"]
assert not stage.exists()
stage.mkdir()
app = stage / "TopxAI Desktop.app"
app.mkdir()
with tarfile.open(bundle) as archive:
    raw = archive.extractfile("manifest.json").read()
    manifest = json.loads(raw)
    entries = manifest["entries"]
    for row in entries:
        name = relative(row["path"])
        destination = app / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        assert app.resolve() in destination.parent.resolve().parents or destination.parent.resolve() == app.resolve()
        if row["kind"] == "directory":
            destination.mkdir(exist_ok=True)
            destination.chmod(row["mode"])
        elif row["kind"] == "symlink":
            target = Path(row["target"])
            assert not target.is_absolute()
            resolved = (destination.parent / target).resolve()
            assert app.resolve() in resolved.parents or resolved == app.resolve()
            destination.symlink_to(row["target"])
        else:
            if row["transfer"] in ("copy", "patch"):
                original = basis / name
                assert original.is_file() and not original.is_symlink()
                assert digest(original) == row["basis_sha256"], str(name)
            if row["transfer"] == "copy":
                shutil.copyfile(original, destination)
            else:
                payload = archive.extractfile(str(relative(row["payload"]))).read()
                data = patch(original.read_bytes(), payload) if row["transfer"] == "patch" else payload
                destination.write_bytes(data)
            destination.chmod(row["mode"])
    for source, name in [("installer-readme.txt", "使用说明.txt"), ("THIRD-PARTY-NOTICES.txt", "THIRD-PARTY-NOTICES.txt")]:
        (stage / name).write_bytes(archive.extractfile(source).read())
    (stage / "Applications").symlink_to("/Applications")
verify(app, entries)
Path("verified-app-manifest.json").write_bytes(raw)
print(json.dumps({"version": manifest["version"], "entries": len(entries), "manifestSha256": hashlib.sha256(raw).hexdigest(), "allAppFilesVerified": True}))
