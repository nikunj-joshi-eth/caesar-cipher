"""
Core Caesar Cipher logic.

Kept intentionally free of I/O so it's easy to unit-test and reuse
from the CLI, a notebook, or a web layer later on.
"""

ALPHABET_SIZE = 26


def _shift_char(ch: str, shift: int) -> str:
    # Only letters shift; everything else (digits, spaces, punctuation)
    # passes through unchanged. This matches the "classic" Caesar behaviour
    # most people expect.
    if "a" <= ch <= "z":
        base = ord("a")
    elif "A" <= ch <= "Z":
        base = ord("A")
    else:
        return ch

    # `% ALPHABET_SIZE` here handles negative shifts and shifts > 25
    # in one line — Python's modulo is well-behaved for negatives.
    return chr((ord(ch) - base + shift) % ALPHABET_SIZE + base)


def encrypt(text: str, shift: int) -> str:
    """Encrypt `text` using a Caesar shift of `shift` positions."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(shift, int):
        raise TypeError("shift must be an integer")

    return "".join(_shift_char(c, shift) for c in text)


def decrypt(text: str, shift: int) -> str:
    """Decrypt `text` that was encrypted with the given shift."""
    return encrypt(text, -shift)


def brute_force(text: str):
    """Yield every possible (shift, decrypted_text) pair.

    Useful when the key is unknown — a human can then eyeball the
    output and pick the readable one.
    """
    for s in range(1, ALPHABET_SIZE):
        yield s, decrypt(text, s)
