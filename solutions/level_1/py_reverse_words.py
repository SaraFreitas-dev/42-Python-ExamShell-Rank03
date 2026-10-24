def reverse_words(text: str) -> str:
    new_text: str = ""
    str_lst: list[str] = text.split()
    
    if not str_lst:
        return new_text

    i: int = len(str_lst) - 1
    while i >= 0:
        new_text += str_lst[i]
        if i >= 1:
            new_text += " "
        i -= 1
    return new_text
            
        
if __name__ == "__main__":
    print(reverse_words("hello world"))           # world hello
    print(reverse_words("  the sky   is blue "))  # blue is sky the
    print(reverse_words("a b c"))                 # c b a
    print(reverse_words("one"))                   # one
    print(reverse_words("   "))                   # (linha vazia)
    print(reverse_words(""))                      # (linha vazia)  