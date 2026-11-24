"""Write one dad joke to /output/entry.txt.

Deterministic: a constant string, no randomness, no time, no network.
The joke itself is the entry; the program only delivers it verbatim.
"""
from pathlib import Path

JOKE = "My dad says being a dad is a vicious cycle \u2014 you blame the kids, the kids blame you, and round and round it goes. Like a bicycle, but with more yelling."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
