def twist_sequence(arr: list[int], k: int) -> list[int]:
    """
    rotates an array to the right by k positions.
    Rotating right by k means the last k elements move to the front.
    """
    if not arr:
        return []
    k %= len(arr)
    return arr[-k:] + arr[:-k]


if __name__ == "__main__":
    print(twist_sequence([1,2,3,4,5], 2))
    print(twist_sequence([1,2,3], 1))
    print(twist_sequence([1,2,3], 5))
    print(twist_sequence([], 3))
