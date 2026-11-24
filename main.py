"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Python 3.13, standard library only.
"""

import os

LINE = "My password manager autofilled my password on a phishing site, then sent me a security tip about never trusting password managers."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters.
assert 1 <= len(LINE) <= 280


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
