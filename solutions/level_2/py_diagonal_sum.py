def diagonal_sum(matrix: list[list[int]]) -> int:
    right: int = len(matrix) - 1
    left: int = 0
    res: int = 0
    for line in matrix:
        res += line[left]
        if right != left:
            res += line[right]
        right -= 1
        left += 1
    return res
    
    
if __name__ == "__main__":
    print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 25
    print(diagonal_sum([[1, 2], [3, 4]]))                   # 10
    print(diagonal_sum([[5]]))                              # 5
    print(diagonal_sum([[-1, 0], [0, -1]]))                 # -2
    print(diagonal_sum([]))                                 # 0