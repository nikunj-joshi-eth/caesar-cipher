# Release v1.0.0 — Caesar Cipher

**Tag:** `v1.0.0`
**Title:** Caesar Cipher v1.0.0 — Initial Stable Release

## Description

First stable release of the Caesar Cipher CLI — a small, dependency-free
Python tool for encrypting, decrypting, and brute-forcing classical
Caesar-shifted text. Suitable for learning, demos, and lightweight scripting.

## Features Added

- Core `encrypt`, `decrypt`, and `brute_force` API in `caesar_cipher.cipher`
- Case-preserving letter shifting; digits, spaces and punctuation pass through
- Correct handling of negative and out-of-range shifts via modulo 26
- Argparse-based CLI with `--encrypt`, `--decrypt`, `--brute`, `--text`, `--shift`
- Interactive fallback mode when no flags are supplied
- 12 pytest cases covering roundtrips, wraparound, negatives, and type errors
- Example script under `examples/demo.py`
- MIT license, README with logo, and clean folder layout

## Known Limitations

- Alphabet limited to A–Z / a–z (ASCII); non-Latin scripts pass through unchanged
- Brute-force mode does not auto-rank candidates by likelihood
- No file I/O flags yet — text is passed via `--text` or stdin prompt
- No packaging on PyPI in this release

## Upgrade Path

This is the initial release, so there is nothing to upgrade from. Future
`1.x` releases will preserve the public API of `caesar_cipher.cipher`
(`encrypt`, `decrypt`, `brute_force`); CLI flag names will remain
backwards-compatible within the `1.x` line.

## Install

```bash
git clone https://github.com/nikunj-joshi-eth/caesar-cipher.git
cd caesar-cipher
pip install -r requirements-dev.txt
pytest -v
python main.py --encrypt --shift 3 --text "Hello, World!"
```