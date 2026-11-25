"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Python 3.13, standard library only.
"""

import os

# Swap 2026-11-25 (Kandidat 3, 87 karakter): ronde 4 peringkat 1.402/2.273,
# ronde 5 2.136/3.015 — di luar 500 besar. Line baru: satu adegan konkret
# (GPS) + twist di frasa terakhir (tol untuk jalan pintas yang ia ciptakan).
LINE = "My GPS rerouted me around traffic, then charged me a toll for the shortcut it invented."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters.
assert 1 <= len(LINE) <= 280


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
