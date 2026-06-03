def cryptic_sorter(strings: list[str]) -> list[str]:
    """
    sorts a list of strings according to multiple criteria:
    1. Primary sort  : By string length (shortest first)
    2. Secondary sort: Alphabetically (for strings of same length)
    3. Tertiary sort : By number of vowels ascending
    """
    return sorted(
        strings, key=lambda word:
        (len(word),
         word.lower(),
         sum(c.lower() in 'aeiou' for c in word)
         )
    )


if __name__ == "__main__":
    print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
    print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
    print(cryptic_sorter(["hello","world","hi","test"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter([""]))