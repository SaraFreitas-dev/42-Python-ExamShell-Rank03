def run_length_encode(text: str) -> str:
    encoded_text: str = ""
    counter: int = 1
    for i in range(1, len(text)):        
        if text[i] == text[i - 1]:
            counter += 1
        else:
            encoded_text += (text[i - 1] + str(counter))
            counter = 1
    if text:
        encoded_text += (text[-1] + str(counter))
    return encoded_text


if __name__ == "__main__":
    print(run_length_encode("aaabcc"))        # a3b1c2
    print(run_length_encode("a"))             # a1
    print(run_length_encode("aAa"))           # a1A1a1
    print(run_length_encode("zzzzzzzzzzzz"))  # z12
    print(run_length_encode("aa  b"))         # a2 2b1
    print(run_length_encode(""))              # (empty line)