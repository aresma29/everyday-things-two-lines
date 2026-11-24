"""Print the two-line entry for Everyday Things, Two Lines, Longer Run."""

from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.txt"


def main() -> None:
    # Print the entry exactly as written: both lines, one sentence each.
    print(ENTRY.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
