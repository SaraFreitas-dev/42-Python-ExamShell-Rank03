def rotate_train(lst: list[int], n: int) -> list[int]: # type: ignore
    """
    The function must rotate the list to the right n times.
    The last elements become the first elements.
    If n is bigger than the list size,
    the function must still work correctly.
    """
    return lst[-n:] + lst[:-n]


if __name__ == "__main__":
    print(rotate_train([1,2,3,4,5], 2))
    print(rotate_train([1,2,3], 0))
