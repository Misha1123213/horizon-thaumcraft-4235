#!/usr/bin/env python3
"""Audit/extract a local Thaumcraft jar without committing its contents.

Usage:
  python3 tools/audit_thaumcraft.py --jar Thaumcraft_1.7.10_4.2.3.5.jar --out build/audit.md
  python3 tools/audit_thaumcraft.py --jar Thaumcraft_1.7.10_4.2.3.5.jar --extract content/thaumcraft
"""
from __future__ import annotations
import argparse, collections, hashlib, os, zipfile
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--jar', required=True)
    ap.add_argument('--out', default='build/audit.md')
    ap.add_argument('--extract', default=None, help='local output root for generated assets/data; ignored by git')
    args = ap.parse_args()
    jar = Path(args.jar)
    if not jar.exists():
        raise SystemExit(f'jar not found: {jar}')
    z = zipfile.ZipFile(jar)
    names = z.namelist()
    files = [n for n in names if not n.endswith('/')]
    ext = {}
    top = {}
    packages = {}
    for n in files:
        e = os.path.splitext(n)[1].lower() or '(noext)'
        ext[e] = ext.get(e, 0) + 1
        t = n.split('/')[0]
        top[t] = top.get(t, 0) + 1
        if n.endswith('.class'):
            pkg = '/'.join(n.split('/')[:-1])
            packages[pkg] = packages.get(pkg, 0) + 1
    sha = hashlib.sha256(jar.read_bytes()).hexdigest()
    out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8') as f:
        f.write(f'# Thaumcraft audit\n\njar: `{jar.name}`\nsha256: `{sha}`\nentries: {len(files)}\n\n')
        f.write('## extensions\n')
        for k, v in sorted(ext.items(), key=lambda kv: (-kv[1], kv[0])): f.write(f'- `{k}`: {v}\n')
        f.write('\n## top-level\n')
        for k, v in sorted(top.items(), key=lambda kv: (-kv[1], kv[0])): f.write(f'- `{k}`: {v}\n')
        f.write('\n## largest class packages\n')
        for k, v in sorted(packages.items(), key=lambda kv: (-kv[1], kv[0]))[:120]: f.write(f'- `{k}`: {v}\n')
    print(out)
    if args.extract:
        root = Path(args.extract)
        count = 0
        for n in files:
            if n.startswith('assets/') or n in ('pack.mcmeta',):
                dest = root / n
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(z.read(n)); count += 1
        print(f'extracted {count} local files under {root} (git-ignored)')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
