def count_palindrome_words(text: str) -> int:
    counter: int = 0
    text_lst: list[str] = text.split()
    
    for word in text_lst:
        if word.lower() == word[::-1].lower():
            counter += 1
    return counter


if __name__ == "__main__":
    print(count_palindrome_words("Anna saw a racecar"))  # 3
    print(count_palindrome_words("Level   noon"))        # 2
    print(count_palindrome_words("Bob"))                 # 1
    print(count_palindrome_words("hello world"))         # 0
    print(count_palindrome_words("abc cba"))             # 0
    print(count_palindrome_words(""))                    # 0
