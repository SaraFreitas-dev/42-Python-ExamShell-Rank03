def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Write a function that mirrors a 2D
    matrix horizontally by reversing each row
    """
    for num_lst in matrix:
        num_lst.reverse()
    return matrix


if __name__ == "__main__":
    print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))
