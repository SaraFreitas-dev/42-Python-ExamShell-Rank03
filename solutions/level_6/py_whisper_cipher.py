def whisper_cipher(text: str, shift: int) -> str:
    """
    Write a function that sorts a list of strings according to multiple criteria:
    1. Primary sort: By string length (shortest first)
    2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
    3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
    4. Equal strings will appear in the same order as in the input list.
    """
    res: str = ""

    for c in text:
        if 'a' <= c <= 'z':
            res += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            res += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            res += c

    return res
