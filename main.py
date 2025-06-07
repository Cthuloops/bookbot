"""A bookbot"""

from stats import (get_word_count, get_character_count, sorted_characters)
import sys


def get_book_text(filepath: str) -> str:
    """Take a filepath and return the contents as a string.

    Parameters
    ----------
    filepath: str
        The file to open.

    Returns
    -------
    str
        The content of the file.
    """

    with open(filepath, "r", encoding="utf8") as f:
        return ''.join(line for line in f)


def pretty_print(filepath: str,
                 content: str, char_list: list[dict[str, str | int]]) -> None:
    """Pretty print the list of char dicts.

    Parameters
    ----------
    filepath: str
        Filepath for file being read.
    content: str
        Content of file.

    char_list: list[dict[str, str | int]]
        List of character dictionaries.
        {"char": character, "num": count}
    """
    print(f"{' BOOKBOT ':=^20}")
    print(f"Analyzing book found at {filepath}")
    print(f"{' Word Count ':-^20}")
    get_word_count(content)
    print(f"{' Character Count ':-^20}")
    for char in char_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print(f"{' END ':=^20}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    content = get_book_text(filepath)
    pretty_print(filepath, content,
                 sorted_characters(get_character_count(content)))


if __name__ == "__main__":
    main()
