def snake_to_camel(text: str) -> str:
    new_txt: list[str] = text.replace("_", " ").split()
    res: str = ""
    
    for i, word in enumerate(new_txt):
        if i == 0:
            res += word.lower()
        else:
            for j, letter in enumerate(word):
                if j == 0:
                    res += letter.upper()
                else:
                    res += letter.lower()
    return res


if __name__ == "__main__":
    print(snake_to_camel("hello_world"))   # helloWorld
    print(snake_to_camel("make_it_work"))  # makeItWork
    print(snake_to_camel("HELLO_WORLD"))   # helloWorld
    print(snake_to_camel("user__id_2"))    # userId2
    print(snake_to_camel("__init__"))      # init
    print(snake_to_camel("already"))       # already
    print(snake_to_camel(""))              # (linha vazia)