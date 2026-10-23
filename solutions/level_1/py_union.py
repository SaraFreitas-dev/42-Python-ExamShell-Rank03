def union(s1: str, s2: str) -> str:
    s_combo: str = ""
    for letter in s1:
        if letter not in s_combo:
            s_combo += letter
    for letter in s2:
        if letter not in s1 and letter not in s_combo:
            s_combo += letter
    return s_combo


if __name__ == "__main__":
    print(union("abc", "bcd"))      # abcd
    print(union("hello", "world"))  # helowrd
    print(union("aaa", ""))         # a
    print(union("", "abc"))         # abc
    print(union("abc", "ABC"))      # abcABC
    print(union("", ""))            # (linha vazia)