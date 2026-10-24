def word_length_sorter(words: list[str]) -> list[str]:
    return sorted(
        words, key=lambda word:
            (
                -len(word),
                word.lower()
            )
    )
    

if __name__ == "__main__":
    print(word_length_sorter(["cat", "banana", "Apple", "dog"]))  # ['banana', 'Apple', 'cat', 'dog']
    print(word_length_sorter(["sun", "moon", "star", "sky"]))     # ['moon', 'star', 'sky', 'sun']
    print(word_length_sorter(["b", "A", "c"]))                    # ['A', 'b', 'c']
    print(word_length_sorter(["Hi", "hi", "HI"]))                 # ['Hi', 'hi', 'HI']
    print(word_length_sorter([]))                                 # []
    print(word_length_sorter([""]))                               # ['']