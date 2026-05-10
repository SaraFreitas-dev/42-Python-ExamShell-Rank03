def mirror_case(s: str) -> str:
    """Alternate the case of each alphabetic character by order
    Non chars remain unchanged"""
    new_s: str = ""
    i = 0
    for char in s:
        if char.isalpha():
            i += 1
            if i % 2 == 0:
                new_s += char.lower()
            else:
                new_s += char.upper()
        else:
            new_s += char
    return new_s


if __name__ == "__main__":
    print(mirror_case("hello!!"))
    print(mirror_case("42 porto"))
    print(mirror_case("a b c"))
