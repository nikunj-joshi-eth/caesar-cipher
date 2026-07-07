#!/usr/bin/env bash
# Recreates a realistic 12-commit history for the Caesar Cipher project.
#
# Usage:
#   1. Unzip the project and `cd caesar-cipher`
#   2. Ensure git identity is set:
#        git config user.name  "Nikunj Joshi"
#        git config user.email "you@example.com"
#   3. Run: bash scripts/build-git-history.sh
#   4. Push: gh repo create caesar-cipher --public --source=. --remote=origin --push
#
# The script snapshots the current working tree, wipes it, then re-adds files
# commit-by-commit so the resulting history looks like organic development.

set -euo pipefail

if [ -d .git ]; then
  echo "Refusing to run: .git already exists. Delete it first if you really want to rebuild history." >&2
  exit 1
fi

SNAPSHOT="$(mktemp -d)"
trap 'rm -rf "$SNAPSHOT"' EXIT

echo "→ Snapshotting current tree to $SNAPSHOT"
shopt -s dotglob
cp -r ./* "$SNAPSHOT"/
shopt -u dotglob

# Wipe working tree (keep the snapshot + this script's own copy safe)
find . -mindepth 1 -maxdepth 1 ! -name '.' ! -name '..' -exec rm -rf {} +

git init -q
git branch -M main

restore() {
  # restore <relative-path-from-project-root> [more paths...]
  for p in "$@"; do
    mkdir -p "$(dirname "$p")"
    cp -r "$SNAPSHOT/$p" "$p"
  done
}

commit() {
  local msg="$1"
  git add -A
  git commit -q -m "$msg"
  echo "  ✓ $msg"
}

echo "→ Building history"

# 1. Repo skeleton
restore .gitignore LICENSE
commit "chore: initialize repository with license and gitignore"

# 2. Package skeleton
mkdir -p src/caesar_cipher tests
restore src/caesar_cipher/__init__.py
# minimal placeholder cipher so imports work
cat > src/caesar_cipher/cipher.py <<'PY'
"""Core Caesar Cipher logic (WIP)."""
ALPHABET_SIZE = 26
PY
commit "feat: scaffold caesar_cipher package"

# 3. Core encrypt
cat > src/caesar_cipher/cipher.py <<'PY'
"""Core Caesar Cipher logic."""
ALPHABET_SIZE = 26


def _shift_char(ch: str, shift: int) -> str:
    if "a" <= ch <= "z":
        base = ord("a")
    elif "A" <= ch <= "Z":
        base = ord("A")
    else:
        return ch
    return chr((ord(ch) - base + shift) % ALPHABET_SIZE + base)


def encrypt(text: str, shift: int) -> str:
    return "".join(_shift_char(c, shift) for c in text)
PY
commit "feat(cipher): implement core encrypt with case preservation"

# 4. Decrypt
cat >> src/caesar_cipher/cipher.py <<'PY'


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)
PY
commit "feat(cipher): add decrypt as inverse of encrypt"

# 5. Brute force + docstrings + input validation (final cipher.py)
restore src/caesar_cipher/cipher.py
commit "feat(cipher): add brute-force mode and input validation"

# 6. First tests
restore tests/test_cipher.py
commit "test: cover encrypt/decrypt, roundtrip, wraparound and negatives"

# 7. CLI
restore src/caesar_cipher/cli.py main.py
commit "feat(cli): argparse interface with interactive fallback"

# 8. Requirements files
restore requirements.txt requirements-dev.txt
commit "chore: pin pytest as dev dependency"

# 9. Example demo
restore examples/demo.py
commit "docs(examples): add runnable demo script"

# 10. Branding: logo
restore assets/logo.svg
commit "chore(assets): add project logo"

# 11. README
restore README.md
commit "docs: write full README with features, usage and learnings"

# 12. Release notes + this script → v1.0.0
restore RELEASE_NOTES.md scripts/build-git-history.sh
commit "release: prepare v1.0.0"

git tag -a v1.0.0 -m "Caesar Cipher v1.0.0 — Initial Stable Release"

echo
echo "✓ Done. History:"
git log --oneline --decorate