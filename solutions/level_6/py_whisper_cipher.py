def whisper_cipher(text: str, shift: int) -> str:
    """
    Creates a Caesar cipher by shifting letters in a
    string by a given amount.
    Non-alphabetic characters should remain unchanged.
    The shift can be negative (shift left).
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

if __name__ == "__main__":
    print(whisper_cipher('hello', 3))
    print(whisper_cipher('ABC123def', 5))
    print( whisper_cipher('abc', -1))
    print(whisper_cipher('abc', 26))