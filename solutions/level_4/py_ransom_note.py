def ransom_note(note: str, letters: str) -> bool:
    letters_dict: dict[str, int] = {}
    for letter in letters:
        if not letter in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1

    for c in note:
        if c.isspace():
            continue
        if not c in letters_dict or letters_dict[c] <= 0:
            return False
        else:
            letters_dict[c] -= 1
    return True


if __name__ == "__main__":
    print(ransom_note("aa", "ab"))                   # False
    print(ransom_note("aa", "ab"))                   # False
    print(ransom_note("hello world", "dlrowolleh"))  # True
    print(ransom_note("Hi", "hi"))                   # False
    print(ransom_note("", "abc"))                    # True
    print(ransom_note("abc", ""))                    # False
