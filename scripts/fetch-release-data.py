#!/usr/bin/env python3
"""Restore the preserved v1.0.0 input files, verifying archives and each file."""
import argparse
import hashlib
import json
from pathlib import Path
import tarfile
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://github.com/leeahwi/graduation-vision/releases/download/v1.0.0"


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def restore(archive_dir):
    manifest = json.loads((ROOT / "docs/releases/data-manifest.json").read_text())
    for name, details in manifest.items():
        archive = archive_dir / name
        if not archive.exists():
            print("Downloading", name, flush=True)
            urllib.request.urlretrieve(f"{BASE_URL}/{name}", archive)
        if digest(archive) != details["sha256"]:
            raise ValueError(f"Archive checksum mismatch: {name}")
        # Validate the entire member set and bytes before writing any file.
        with tarfile.open(archive, "r:gz") as bundle:
            members = bundle.getmembers()
            if {member.name for member in members} != set(details["files"]) or len(members) != len(details["files"]):
                raise ValueError(f"Unexpected archive members: {name}")
            verified = {}
            for member in members:
                if not member.isfile():
                    raise ValueError(f"Not a regular file: {member.name}")
                content = bundle.extractfile(member).read()
                if hashlib.sha256(content).hexdigest() != details["files"][member.name]:
                    raise ValueError(f"File checksum mismatch: {member.name}")
                verified[member.name] = content
            for relative, content in verified.items():
                destination = ROOT / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(content)
                print("Verified:", relative)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive-dir", type=Path, help="Use/download archives in this directory")
    args = parser.parse_args()
    if args.archive_dir:
        args.archive_dir.mkdir(parents=True, exist_ok=True)
        restore(args.archive_dir)
    else:
        with tempfile.TemporaryDirectory() as directory:
            restore(Path(directory))
