def pattern_tracker(text: str) -> int:
    """
    Counts the number of valid consecutive digit pairs
    in a string. A valid pair consists of two adjacent
    digits where the second digit is exactly one greater
    than the first. A 9 followed by a 0 is NOT a valid pair.
    """
    counter = 0
    for i in range(len(text) - 1):
        if(
            text[i].isdigit() and
            text[i + 1].isdigit() and
            (int(text[i]) + 1 == int(text[i + 1]))
        ):
            counter += 1
    return counter


if __name__ == "__main__":
    print(pattern_tracker("123"))  # 2
    print(pattern_tracker("12a34"))  # 2
    print(pattern_tracker("1a2b3c4"))  # 0
