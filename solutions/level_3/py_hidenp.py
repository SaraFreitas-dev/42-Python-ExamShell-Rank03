def hidenp(small: str, big: str) -> bool:
    """
    Checks if the string 'small' is a subsequence of 'big'.
    A subsequence means all characters of 'small' appear in 'big'
    in the same order, but not necessarily consecutively.
    """
    it = iter(big)
    return all(c in it for c in small)

if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3"))   # True
    print(hidenp("ace", "abcde"))    # True
    print(hidenp("aec", "abcde"))    # False
    print(hidenp("", "abc"))   # True
    print(hidenp("", ""))      # True
