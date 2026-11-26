"""What the Elevator Would Say — entry program (program/v1).

Writes the entry line to /output/entry.txt and prints it.
"""

SETUP = (
    "My doors have closed on eleven umbrellas, three strollers, "
    "and one wedding dress."
)
TURN = "Only the dress fought back."
LINE = SETUP + " " + TURN


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters.
    assert 1 <= len(LINE) <= 120, "entry outside the 1-120 character gate"
    assert LINE.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
