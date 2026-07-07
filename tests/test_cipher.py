import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest
from caesar_cipher.cipher import encrypt, decrypt, brute_force


def test_basic_encrypt():
    assert encrypt("Hello, World!", 3) == "Khoor, Zruog!"


def test_basic_decrypt():
    assert decrypt("Khoor, Zruog!", 3) == "Hello, World!"


def test_roundtrip():
    text = "The quick brown fox jumps over the lazy dog."
    assert decrypt(encrypt(text, 7), 7) == text


@pytest.mark.parametrize("shift", [0, 26, 52, -26])
def test_full_wraparound_is_identity(shift):
    assert encrypt("abcXYZ", shift) == "abcXYZ"


def test_negative_shift():
    assert encrypt("abc", -1) == "zab"


def test_non_letters_untouched():
    assert encrypt("123 !@# \n", 10) == "123 !@# \n"


def test_case_preserved():
    assert encrypt("AbCdEf", 1) == "BcDeFg"


def test_brute_force_finds_original():
    original = "Attack at dawn"
    cipher = encrypt(original, 11)
    assert any(guess == original for _, guess in brute_force(cipher))


def test_type_errors():
    with pytest.raises(TypeError):
        encrypt(123, 3)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        encrypt("hi", "3")  # type: ignore[arg-type]
