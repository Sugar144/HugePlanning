"""Generate small deterministic package-security fixtures in a caller-owned temp root."""

from __future__ import annotations

from pathlib import Path
import stat
import struct
import zipfile


def write_zip(path: Path, entries: list[tuple[str, bytes]], *, symlink: bool = False, device: bool = False, compression=zipfile.ZIP_STORED) -> Path:
    with zipfile.ZipFile(path, "w", compression=compression) as archive:
        for index, (name, data) in enumerate(entries):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = compression
            mode = (stat.S_IFLNK | 0o777) if symlink and index == 0 else ((stat.S_IFCHR | 0o600) if device and index == 0 else (stat.S_IFREG | 0o644))
            info.external_attr = mode << 16
            archive.writestr(info, data)
    return path


def mark_encrypted(path: Path) -> Path:
    data = bytearray(path.read_bytes())
    offset = 0
    while True:
        offset = data.find(b"PK\x03\x04", offset)
        if offset < 0: break
        flags = struct.unpack_from("<H", data, offset + 6)[0] | 1
        struct.pack_into("<H", data, offset + 6, flags); offset += 4
    offset = 0
    while True:
        offset = data.find(b"PK\x01\x02", offset)
        if offset < 0: break
        flags = struct.unpack_from("<H", data, offset + 8)[0] | 1
        struct.pack_into("<H", data, offset + 8, flags); offset += 4
    path.write_bytes(data)
    return path


def generate(root: Path) -> dict[str, Path]:
    root.mkdir(parents=True, exist_ok=True)
    cases = {
        "missing_member": write_zip(root / "missing.zip", [("a.txt", b"a")]),
        "extra_member": write_zip(root / "extra.zip", [("a.txt", b"a"), ("extra.txt", b"x")]),
        "duplicate_normalized": write_zip(root / "duplicate.zip", [("a/b.txt", b"a"), ("a//b.txt", b"b")]),
        "wrong_hash": write_zip(root / "wrong-hash.zip", [("a.txt", b"wrong")]),
        "traversal": write_zip(root / "traversal.zip", [("../escape", b"x")]),
        "absolute": write_zip(root / "absolute.zip", [("/escape", b"x")]),
        "backslash": write_zip(root / "backslash.zip", [("a\\b", b"x")]),
        "symlink": write_zip(root / "symlink.zip", [("link", b"target")], symlink=True),
        "device": write_zip(root / "device.zip", [("device", b"x")], device=True),
        "encrypted": mark_encrypted(write_zip(root / "encrypted.zip", [("a.txt", b"a")])),
        "excessive_members": write_zip(root / "members.zip", [(f"{i}.txt", b"x") for i in range(5)]),
        "excessive_size": write_zip(root / "size.zip", [("big.txt", b"x" * 1024)]),
        "excessive_ratio": write_zip(root / "ratio.zip", [("ratio.txt", b"0" * 20000)], compression=zipfile.ZIP_DEFLATED),
        "invalid_utf8": write_zip(root / "utf8.zip", [("data.yaml", b"\xff")]),
        "duplicate_yaml_key": write_zip(root / "duplicate-yaml.zip", [("data.yaml", b"a: 1\na: 2\n")]),
    }
    return cases
