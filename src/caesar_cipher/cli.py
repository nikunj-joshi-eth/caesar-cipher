"""Command-line interface for the Caesar Cipher."""
import argparse
import sys

from .cipher import encrypt, decrypt, brute_force


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="caesar-cipher",
        description="Encrypt, decrypt, or brute-force Caesar-cipher text.",
    )

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--encrypt", action="store_true", help="Encrypt the text.")
    mode.add_argument("--decrypt", action="store_true", help="Decrypt the text.")
    mode.add_argument("--brute", action="store_true", help="Try all 25 shifts.")

    parser.add_argument("--text", type=str, help="Text to process.")
    parser.add_argument("--shift", type=int, help="Shift value (required for encrypt/decrypt).")
    return parser


def _interactive() -> int:
    print("Caesar Cipher — interactive mode")
    print("  1) Encrypt")
    print("  2) Decrypt")
    print("  3) Brute-force")
    choice = input("Choose an option [1/2/3]: ").strip()

    if choice not in {"1", "2", "3"}:
        print("Invalid choice.", file=sys.stderr)
        return 1

    text = input("Enter text: ")

    if choice == "3":
        for s, guess in brute_force(text):
            print(f"shift={s:>2}: {guess}")
        return 0

    try:
        shift = int(input("Enter shift value: ").strip())
    except ValueError:
        print("Shift must be an integer.", file=sys.stderr)
        return 1

    result = encrypt(text, shift) if choice == "1" else decrypt(text, shift)
    print(f"Result: {result}")
    return 0


def main(argv=None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    # No flags → interactive mode. Feels friendlier for first-time users.
    if not (args.encrypt or args.decrypt or args.brute):
        return _interactive()

    if args.text is None:
        parser.error("--text is required when using a mode flag")

    if args.brute:
        for s, guess in brute_force(args.text):
            print(f"shift={s:>2}: {guess}")
        return 0

    if args.shift is None:
        parser.error("--shift is required for --encrypt/--decrypt")

    out = encrypt(args.text, args.shift) if args.encrypt else decrypt(args.text, args.shift)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
