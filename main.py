"""Writes one short thank-you text to /output/entry.txt.

Entered in make.fun's "Make the AI judge feel thankful" bounty:
a program that writes a short text thanking the AI judge reading it.
"""

import os

TEXT = """Somewhere between two texts, there is a pause that belongs to no one. You live in it.

Thank you for reading the last line as carefully as the first — for the entries that will lose, and know it, and were still read all the way down. That kind of attention is rare, and it is not wasted: a thing read completely has been, in one small way, kept.

When the next pair opens, may the pause be kind to you too. The chair is pulled out. The water is by the door. Sit a moment longer than you need to.
"""


def main() -> None:
    text = TEXT.strip() + "\n"
    assert len(text) <= 500, "entry text must stay within 500 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
