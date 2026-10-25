def atbash_cipher(text: str) -> str:
    new_text: str = ""
    for letter in text:
        if letter >= 'a' and letter <= 'z':
            new_text += chr(ord('a') + (ord('z') - ord(letter)))
        elif letter >= 'A' and letter <= 'Z':
                    new_text += chr(ord('A') + (ord('Z') - ord(letter)))
        else:
            new_text += letter
    return new_text


if __name__ == "__main__":
    print(atbash_cipher("abc"))           # zyx
    print(atbash_cipher("Hello World!"))  # Svool Dliow!
    print(atbash_cipher("xyz123"))        # cba123
    print(atbash_cipher("Zz"))            # Aa
    print(atbash_cipher(""))              # (linha vazia)