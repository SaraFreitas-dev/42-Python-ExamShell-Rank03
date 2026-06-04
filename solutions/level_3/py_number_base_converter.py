def number_base_converter(number: str,
                          from_base: int,
                          to_base: int) -> str:
    """
    Converts a number from one base to another.
    Support bases from 2 to 36 inclusive.
    Use digits 0-9 and letters A-Z for values 10-35.
    Return "ERROR" for invalid inputs
    """
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not 2 <= from_base <= 36:
        return "ERROR"
    if not 2 <= to_base <= 36:
        return "ERROR"
    try:
        decimal = int(number, from_base)
    except ValueError:
        return ("ERROR")
    if decimal == 0:
        return "0"
    result: str = ""
    while decimal > 0:
        result = digits[decimal % to_base] + result
        decimal //= to_base
    return result


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))  # 10
    print(number_base_converter("255", 10, 16))  # FF
    print(number_base_converter("123", 1, 10))  # ERROR