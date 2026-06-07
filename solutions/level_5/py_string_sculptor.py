def string_sculptor(text: str) -> str:
    """
    Transforms a string by alternating the case
    of alphabetic characters only.
    Non-alphabetic characters remain unchanged and are
    NOT counted in the alternation index.
    The first alphabetic character should be lowercase,
    the second uppercase, etc. Spaces reset the alternation
    (next alpha after a space is lowercase again).
    """
    to_low: bool = True
    res: str = ""
    for i in range(len(text)):
        if text[i].isspace():
            to_low = True
        if text[i].isalpha():
            if to_low:
                res += text[i].lower()
                to_low = False
            else:
                res += text[i].upper()
                to_low = True
        else:
            res += text[i]
    return res

if __name__ == "__main__":
    print(string_sculptor("Hello World!"))  # "hElLo wOrLd"
    print(string_sculptor("abc123def"))  # "aBc123DeF"
