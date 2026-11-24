"""Famous Last Words at 1 Percent — make.fun entry program.

Writes one line — the funniest last words a phone says as its battery
hits 1 percent — to /output/entry.txt, with no trailing newline.

Stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "I outlasted his last relationship, his gym membership, and "
    "every New Year's resolution \u2014 and I still don't get a thank you."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    # Gate guard: the sealed scorer only accepts UTF-8 text of 1 to 199
    # characters, not only white space, on a single line. Fail loudly
    # here instead of shipping an entry the gate would refuse.
    assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    ENTRY.encode("utf-8")

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
