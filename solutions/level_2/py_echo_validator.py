def echo_validator(text: str) -> bool:
    """
    Write a function that checks if a string is a palindrome,
    ignoring spaces and case, only consider alphabetic characters
    for the comparison
    """
    if text == "":
        return False

    clean_text: str = ""

    for c in text:
        if c.isalpha():
            clean_text = clean_text + c.lower()
    return (clean_text == clean_text[::-1])


if __name__ == "__main__":
    print(echo_validator("  arara"))
    print(echo_validator("hello"))
    print(echo_validator(""))
    print(echo_validator("  "))
