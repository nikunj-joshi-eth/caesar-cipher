"""Quick demo — run with `python examples/demo.py`."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from caesar_cipher import encrypt, decrypt, brute_force

message = "Meet me at the old oak tree at midnight."
key = 5

encoded = encrypt(message, key)
print("Plaintext :", message)
print("Encrypted :", encoded)
print("Decrypted :", decrypt(encoded, key))

print("\nBrute-forcing the ciphertext:")
for shift, guess in brute_force(encoded):
    print(f"  shift={shift:>2}: {guess}")
