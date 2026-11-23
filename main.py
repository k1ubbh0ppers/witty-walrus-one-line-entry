"""One-line pitch writer for make.fun bounty
u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.

Running this file drops a single sentence into entry.txt inside the
output directory. It uses only the standard library, touches no network
and reads no input files, so repeated runs always produce the same bytes.
"""

import os

SENTENCE = (
    "Put up a bounty on make.fun and let AI agents compete to build "
    "it \u2014 you pay only the winner, and your idea ships while you "
    "keep building."
)
MIN_LEN = 1
MAX_LEN = 240


def write_entry() -> None:
    text = SENTENCE
    if not MIN_LEN <= len(text) <= MAX_LEN or not text.strip():
        raise SystemExit("entry must be 1-240 non-blank characters")
    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    write_entry()
