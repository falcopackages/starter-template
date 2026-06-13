from __future__ import annotations

import argparse
import os
import platform
import shutil
import stat
import tarfile
import tempfile
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PACKAGE_BY_PLATFORM = {
    ("Linux", "x86_64"): "@esbuild/linux-x64",
    ("Linux", "AMD64"): "@esbuild/linux-x64",
    ("Linux", "aarch64"): "@esbuild/linux-arm64",
    ("Linux", "arm64"): "@esbuild/linux-arm64",
    ("Darwin", "x86_64"): "@esbuild/darwin-x64",
    ("Darwin", "arm64"): "@esbuild/darwin-arm64",
}


def package_url(package: str, version: str) -> str:
    scope, name = package.split("/")
    escaped = f"{scope}%2f{name}"
    return f"https://registry.npmjs.org/{escaped}/-/{name}-{version}.tgz"


def detect_package() -> str:
    system = platform.system()
    machine = platform.machine()
    package = PACKAGE_BY_PLATFORM.get((system, machine))
    if package is None:
        raise SystemExit(f"Unsupported esbuild platform: {system} {machine}")
    return package


def install_esbuild(version: str) -> None:
    package = detect_package()
    url = package_url(package, version)
    destination = ROOT / "bin" / f"esbuild-{version}"

    if destination.is_file() and os.access(destination, os.X_OK):
        print(os.fspath(destination.relative_to(ROOT)))
        return

    destination.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        archive_path = Path(tmp) / "esbuild.tgz"
        urllib.request.urlretrieve(url, archive_path)
        with tarfile.open(archive_path) as archive:
            archive.extract("package/bin/esbuild", tmp, filter="data")

        extracted = Path(tmp) / "package" / "bin" / "esbuild"
        shutil.move(extracted, destination)

    mode = destination.stat().st_mode
    destination.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print(os.fspath(destination.relative_to(ROOT)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    args = parser.parse_args()
    install_esbuild(args.version)


if __name__ == "__main__":
    main()
