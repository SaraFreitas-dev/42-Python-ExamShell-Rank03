def first_unique_char(s: str) -> int:
    s_dict: dict[str, int] = {}
    
    for letter in s:
        if not letter in s_dict:
            s_dict[letter] = 1
        else:
            s_dict[letter] += 1
    for i, v in enumerate(s):
        if s_dict[v] == 1:
            return i
    return -1
    
if __name__ == "__main__":
    print(first_unique_char("leetcode"))      # 0
    print(first_unique_char("aabbc"))         # 4
    print(first_unique_char("loveleetcode"))  # 2
    print(first_unique_char("aabb"))          # -1
    print(first_unique_char("aA"))            # 0
    print(first_unique_char("z"))             # 0
    print(first_unique_char(""))              # -1