#!/usr/bin/env python3
"""Build Extreme-Gammon-for-Mac.zip with Unix execute bits preserved."""
from pathlib import Path
import zipfile
import sys

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "app" / "Extreme Gammon.app"
HOW = ROOT / "How to open this.txt"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist" / "Extreme-Gammon-for-Mac.zip"
OUT.parent.mkdir(parents=True, exist_ok=True)

def add_dir(zf, arc):
    zi = zipfile.ZipInfo(arc if arc.endswith("/") else arc + "/")
    zi.create_system = 3
    zi.external_attr = (0o40755 << 16)
    zf.writestr(zi, b"")

def add_file(zf, path: Path, arc: str, executable=False):
    zi = zipfile.ZipInfo(arc)
    zi.create_system = 3
    zi.compress_type = zipfile.ZIP_DEFLATED
    zi.external_attr = ((0o100755 if executable else 0o100644) << 16)
    zf.writestr(zi, path.read_bytes())

if OUT.exists():
    OUT.unlink()

prefix = "Extreme Gammon for Mac"
with zipfile.ZipFile(OUT, "w") as zf:
    add_dir(zf, prefix + "/")
    add_file(zf, HOW, f"{prefix}/How to open this.txt")
    for p in sorted(APP.rglob("*")):
        rel = p.relative_to(APP.parent).as_posix()
        arc = f"{prefix}/{rel}"
        if p.is_dir():
            add_dir(zf, arc)
        else:
            add_file(zf, p, arc, executable=(p.name == "ExtremeGammon"))
print(OUT)
