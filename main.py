"""Six Words, One Story entry.

Writes one original six-word story to /output/entry.txt. The story is a
fixed string: the program is deterministic on purpose, so every run
produces the exact same entry, byte for byte.
"""

import os

STORY = "He faked his death. She applauded."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 60
WORD_COUNT = 6


def validate(story):
    """The gate only accepts UTF-8 text of 1 to 60 chars, not only whitespace,
    and the brief asks for a complete story in exactly six words."""
    if not story or not story.strip():
        raise ValueError("story is empty")
    if len(story) > MAX_CHARS:
        raise ValueError(f"story is {len(story)} chars, over the {MAX_CHARS} limit")
    words = story.split()
    if len(words) != WORD_COUNT:
        raise ValueError(f"story has {len(words)} words, expected {WORD_COUNT}")
    story.encode("utf-8")
    return story


def main():
    story = validate(STORY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(story)
    # Round-trip: the file the judge reads must be byte-identical to STORY.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != story:
        raise ValueError("written entry differs from the story")
    print(f"Wrote {len(story)} chars, {len(story.split())} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
