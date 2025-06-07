"""Statistical analysis functions"""


def get_word_count(text: str) -> None:
    """Count and print the amount of words in a string.

    Parameters
    ----------
    text: str
        String to count words.
    """

    print(f"Found {len(text.split())} total words")


def get_character_count(text: str) -> dict[str, int]:
    """Count the amount of occurences for each character in the text.

    Parameters
    ----------
    text: str
        String to count characters

    Returns
    -------
    dict[str, int]
        Dictionary where the key is the character and the value is the count
        of character found in the text.
    """
    char_dict = {}

    for char in text.casefold():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sorted_characters(characters: dict[str, int]) -> list[dict[str, int | str]]:
    """Transform a dictionary of characters into a sorted list of dictionaries.

    Parameters
    ----------
    characters: dict[str, int]
        Dictionary of characters and their counts.

    Returns
    -------
    list[dict[str, int | str]]
        Sorted list of dictionaries
    """
    dict_list: list[dict[str, str | int]] = []

    for key, value in characters.items():
        dict_list.append({"char": key, "num": value})

    dict_list.sort(reverse=True, key=lambda x: x["num"])

    return dict_list
