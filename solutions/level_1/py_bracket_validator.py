def bracket_validator(s: str) -> bool:
    """
    checks if the brackets in a string are valid.
    A string is valid if every opening bracket
    has a matching closing bracket in the correct order.
    """
    stack: list[str] = []
    pairs: dict[str, str] = {"(": ")",
                             "[": "]",
                             "{": "}"}
    for bracket in s:
        if bracket in pairs:  # Opening bracket
            stack.append(bracket)
        elif bracket in pairs.values():  # Closing bracket
            if not stack:
                return False
            if pairs[stack.pop()] != bracket:  # pairs[stack.pop()] meaning the last opened bracket
                return False

    # To be true, the stack must be empty at the end
    return len(stack) == 0

if __name__ == "__main__":
    print(bracket_validator("()"))
    print(bracket_validator("()[]{}"))
    print(bracket_validator("(]"))
    print(bracket_validator("hello(world)"))
