"""Write one dad joke to /output/entry.txt.

Deterministic: a constant string, no randomness, no time, no network.
The joke itself is the entry; the program only delivers it verbatim.
"""
from pathlib import Path

JOKE = "My dad says he doesn't need a smartwatch. He already has me \u2014 I remind him of everything, twice, loudly, from the next room."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
