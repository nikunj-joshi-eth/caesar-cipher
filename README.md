<div align="center">

<img src="assets/logo.svg" alt="Caesar Cipher" width="120"/>

# Caesar Cipher

A clean, well-tested Python implementation of the classic Caesar cipher — usable as a **CLI** or an **importable library**.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/github/license/nikunj-joshi-eth/caesar-cipher)
![Release](https://img.shields.io/github/v/release/nikunj-joshi-eth/caesar-cipher)
![Stars](https://img.shields.io/github/stars/nikunj-joshi-eth/caesar-cipher?style=social)

</div>

---

## ✨ Features

- 🔐 Encode & decode any text with a configurable shift
- 🔤 Handles upper/lowercase, preserves punctuation, digits, and spaces
- 🌀 Correct wrap-around across the alphabet (`z + 1 → a`)
- 🧪 Full test coverage with `pytest`, including edge cases
- 🖥️ Simple CLI powered by `argparse`
- 📦 Zero runtime dependencies

---

## 🚀 Quick start

### Install

```bash
git clone https://github.com/nikunj-joshi-eth/caesar-cipher.git
cd caesar-cipher
pip install -r requirements.txt
```

### Use the CLI

```bash
python main.py encode --shift 3 --text "Hello, World!"
# → Khoor, Zruog!

python main.py decode --shift 3 --text "Khoor, Zruog!"
# → Hello, World!
```

### Use as a library

```python
from caesar_cipher.cipher import encode, decode

encode("Attack at dawn", shift=7)   # 'Haahjr ha khdu'
decode("Haahjr ha khdu", shift=7)   # 'Attack at dawn'
```

---

## 🧪 Running tests

```bash
pip install -r requirements-dev.txt
pytest -v
```

---

## 📂 Project structure

```text
caesar-cipher/
├── src/caesar_cipher/     # Core library
│   ├── cipher.py          # encode / decode logic
│   └── cli.py             # CLI entry point
├── tests/                 # Pytest suite
├── examples/demo.py       # Usage demo
├── main.py                # CLI launcher
└── README.md
```

---

## 📖 How it works

The Caesar cipher shifts each letter in the plaintext by a fixed number of positions in the alphabet. With a shift of `3`:

```text
A → D    H → K    Z → C
```

Non-alphabetic characters (spaces, digits, punctuation) pass through unchanged.

---

## 🗺️ Roadmap

- [ ] Brute-force decryption (try all 25 shifts)
- [ ] Frequency-analysis auto-solver
- [ ] Web UI demo

---

## 📜 License

MIT © [Nikunj Joshi](https://github.com/nikunj-joshi-eth)
