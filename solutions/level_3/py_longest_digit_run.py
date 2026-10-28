def longest_digit_run(text: str) -> int:
    counter: int = 0
    best_counter: int = 0

    for i in range(0, len(text)):
        curr_num: str = text[i]
        
        if curr_num < '0' or curr_num > '9':
            counter = 0
        elif curr_num == text[i - 1] and (curr_num >= '0' and curr_num <= '9'):
            counter += 1
        else:
            counter = 1
        if counter > best_counter:
            best_counter = counter
    return best_counter
                
            
if __name__ == "__main__":
    print(longest_digit_run("1112233"))   # 3
    print(longest_digit_run("a1111b22"))  # 4
    print(longest_digit_run("12345"))     # 1
    print(longest_digit_run("77a77"))     # 2
    print(longest_digit_run("999.99"))    # 3
    print(longest_digit_run("abc"))       # 0
    print(longest_digit_run(""))          # 0