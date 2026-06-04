def string_permutation_checker(s1: str, s2: str) -> bool:
    """
    Determines if two strings are permutations of each other.
    Case sensitive. Whitespace and punctuation count as
    regular characters.
    Empty strings are permutations of each other.
    """
    return (sorted(s1) == sorted(s2))


if __name__ == "__main__":
    print(string_permutation_checker("abc", "bca"))
    print(string_permutation_checker("abc", "def"))
    print(string_permutation_checker("", ""))
