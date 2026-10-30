def count_occurrences(sub: str, text: str) -> int:
    counter: int = 0
    i: int = 0
    
    if not sub:
        return counter

    while i < len(text):
        j: int = 0
        while(((i + j) < len(text)) and j < len(sub)):
            if sub[j] == text[i + j]:
                j += 1
            else: 
                break
        if j == len(sub):
            counter += 1
            i += len(sub)
        else:
            i += 1

    return counter


if __name__ == "__main__":
    print(count_occurrences("ab", "ababab"))  # 3
    print(count_occurrences("aa", "aaaa"))    # 2
    print(count_occurrences("aa", "aaa"))     # 1
    print(count_occurrences("Ab", "abAb"))    # 1
    print(count_occurrences("x", "abc"))      # 0
    print(count_occurrences("abc", "ab"))     # 0
    print(count_occurrences("", "abc"))       # 0
