def whisper_cipher(text: str, shift: int) -> str:
    """
    Write a function that creates a simple cipher
    by shifting letters in a str by a given amount.
    Non-alphabetic characters should remain unchanged
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
