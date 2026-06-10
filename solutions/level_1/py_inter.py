def inter(s1: str, s2: str) -> str:
    """
    Returns a string with the characters that appears
    in both strings, without repetitions.
    Characters are added in the order that
    they appear in the first string.
    """
    res: str = ""
    for c in s1:
        if c not in res and c in s2:
            res += c
    return res


if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))