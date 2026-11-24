"""make.fun bounty: One Word, First Thought.

Deterministic, no-network program. Writes exactly one word to
/output/entry.txt: the first word that comes to mind, nothing else.

The word is fireflies: a small warm light you only notice on a
quiet night, vivid enough to stick in your head. No topic, no
explanation, no second draft. Running twice writes identical bytes.
"""
from pathlib import Path

WORD = "fireflies"

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(WORD, encoding="utf-8")
    print(f"Wrote {OUT} ({len(WORD)} chars)")


if __name__ == "__main__":
    main()
