# ─────────────────────────────────────────────────────────────
# EXERCISE BANK - PRACTICE (Rank 03 style)
# Original practice exercises inspired by the exam format.
# These are NOT the real exam subjects.
# ─────────────────────────────────────────────────────────────
EXERCISES = {
    # ── LEVEL 1 ──────────────────────────────────────────────
    "py_word_length_sorter": {
        "level": 1,
        "subject": """\
Assignment name  : py_word_length_sorter
Expected files   : py_word_length_sorter.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that sorts a list of words according to these criteria:
1. Primary sort: By word length (longest first)
2. Secondary sort: Alphabetical order, comparing letters case-insensitively
   (for words of same length)
3. Words that are equal when ignoring case keep the same order as in the
   input list.

Your function must be declared as follows:

    def word_length_sorter(words: list[str]) -> list[str]:

The function should return a new sorted list.

Your function must handle:
  - Empty strings and empty lists
  - Mixed case words (treat as lowercase for sorting)

Examples:
    word_length_sorter(["cat", "banana", "Apple", "dog"])
        -> ["banana", "Apple", "cat", "dog"]
    word_length_sorter(["sun", "moon", "star", "sky"])
        -> ["moon", "star", "sky", "sun"]
    word_length_sorter(["b", "A", "c"])
        -> ["A", "b", "c"]
    word_length_sorter(["Hi", "hi", "HI"])
        -> ["Hi", "hi", "HI"]
    word_length_sorter([])       -> []
    word_length_sorter([""])     -> [""]
""",
        "function": "word_length_sorter",
        "tests": [
            ([["cat", "banana", "Apple", "dog"]], ["banana", "Apple", "cat", "dog"]),
            ([["sun", "moon", "star", "sky"]], ["moon", "star", "sky", "sun"]),
            ([["b", "A", "c"]], ["A", "b", "c"]),
            ([["Hi", "hi", "HI"]], ["Hi", "hi", "HI"]),
            ([[]], []),
            ([[""]], [""]),
            ([["", "a", ""]], ["a", "", ""]),
            ([["Zebra", "apple", "Mango"]], ["apple", "Mango", "Zebra"]),
            ([["ab", "abc", "a"]], ["abc", "ab", "a"]),
        ],
    },

    "py_union": {
        "level": 1,
        "subject": """\
Assignment name  : py_union
Expected files   : py_union.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that returns a string with the characters that appear in
either of the two strings, without repetitions. Characters are added in the
order they first appear: first going through the first string, then through
the second string.

Your function must be declared as follows:

    def union(s1: str, s2: str) -> str:

Examples:
    union("abc", "bcd")         -> "abcd"
    union("hello", "world")     -> "helowrd"
    union("aaa", "")            -> "a"
    union("", "abc")            -> "abc"
    union("abc", "ABC")         -> "abcABC"
    union("", "")               -> ""
""",
        "function": "union",
        "tests": [
            (["abc", "bcd"], "abcd"),
            (["hello", "world"], "helowrd"),
            (["aaa", ""], "a"),
            (["", "abc"], "abc"),
            (["abc", "ABC"], "abcABC"),
            (["", ""], ""),
            (["zpadinton", "paqefwtdjetyiytjneytjoeyjnejeyj"], "zpadintoqefwjy"),
            (["a b", "b c"], "a bc"),
            (["112", "321"], "123"),
        ],
    },

    # ── LEVEL 2 ──────────────────────────────────────────────
    "py_rotate_matrix": {
        "level": 2,
        "subject": """\
Assignment name  : py_rotate_matrix
Expected files   : py_rotate_matrix.py
Allowed functions: None
--------------------------------------------------------------------------------

Given a 2D matrix (list of lists), return a new matrix rotated 90 degrees
clockwise.

The first column of the original matrix (read from bottom to top) becomes the
first row of the new matrix. The matrix does not need to be square.
An empty matrix returns an empty list.

Your function must be declared as follows:

    def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:

Examples:
    rotate_matrix([[1,2],[3,4]])          -> [[3,1],[4,2]]
    rotate_matrix([[1,2,3],[4,5,6]])      -> [[4,1],[5,2],[6,3]]
    rotate_matrix([[1,2,3]])              -> [[1],[2],[3]]
    rotate_matrix([[1],[2],[3]])          -> [[3,2,1]]
    rotate_matrix([[7]])                  -> [[7]]
    rotate_matrix([])                     -> []
""",
        "function": "rotate_matrix",
        "tests": [
            ([[[1, 2], [3, 4]]], [[3, 1], [4, 2]]),
            ([[[1, 2, 3], [4, 5, 6]]], [[4, 1], [5, 2], [6, 3]]),
            ([[[1, 2, 3]]], [[1], [2], [3]]),
            ([[[1], [2], [3]]], [[3, 2, 1]]),
            ([[[7]]], [[7]]),
            ([[]], []),
            ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            ([[[-1, -2], [-3, -4]]], [[-3, -1], [-4, -2]]),
        ],
    },

    "py_diagonal_sum": {
        "level": 2,
        "subject": """\
Assignment name  : py_diagonal_sum
Expected files   : py_diagonal_sum.py
Allowed functions: None
--------------------------------------------------------------------------------

Given a square matrix (list of lists), return the sum of the elements on both
diagonals.

The main diagonal goes from the top-left to the bottom-right corner.
The secondary diagonal goes from the top-right to the bottom-left corner.
If the matrix has an odd size, the center element belongs to both diagonals
and must be counted only once.
An empty matrix returns 0.

Your function must be declared as follows:

    def diagonal_sum(matrix: list[list[int]]) -> int:

Examples:
    diagonal_sum([[1,2,3],[4,5,6],[7,8,9]])   -> 25
    diagonal_sum([[1,2],[3,4]])               -> 10
    diagonal_sum([[5]])                       -> 5
    diagonal_sum([[-1,0],[0,-1]])             -> -2
    diagonal_sum([])                          -> 0
""",
        "function": "diagonal_sum",
        "tests": [
            ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], 25),
            ([[[1, 2], [3, 4]]], 10),
            ([[[5]]], 5),
            ([[[-1, 0], [0, -1]]], -2),
            ([[]], 0),
            ([[[1, 1, 1, 1]] * 4], 8),
            ([[[0, 0, 0], [0, 0, 0], [0, 0, 0]]], 0),
            ([[[2, 9, 2], [9, 3, 9], [2, 9, 2]]], 11),
        ],
    },

    "py_count_palindrome_words": {
        "level": 2,
        "subject": """\
Assignment name  : py_count_palindrome_words
Expected files   : py_count_palindrome_words.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that counts how many words of a sentence are palindromes,
ignoring case.

Words are separated by one or more spaces. A word of a single letter is a
palindrome. An empty string or a string with only spaces has no words.

Your function must be declared as follows:

    def count_palindrome_words(text: str) -> int:

Examples:
    count_palindrome_words("Anna saw a racecar")   -> 3
    count_palindrome_words("Level   noon")         -> 2
    count_palindrome_words("Bob")                  -> 1
    count_palindrome_words("hello world")          -> 0
    count_palindrome_words("abc cba")              -> 0
    count_palindrome_words("")                     -> 0
""",
        "function": "count_palindrome_words",
        "tests": [
            (["Anna saw a racecar"], 3),
            (["Level   noon"], 2),
            (["Bob"], 1),
            (["hello world"], 0),
            (["abc cba"], 0),
            ([""], 0),
            (["   "], 0),
            (["  wow  "], 1),
            (["Madam Civic KAYAK stats"], 4),
        ],
    },

    # ── LEVEL 3 ──────────────────────────────────────────────
    "py_int_to_roman": {
        "level": 3,
        "subject": """\
Assignment name  : py_int_to_roman
Expected files   : py_int_to_roman.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that converts an integer into a Roman numeral.
Support numbers from 1 to 3999 inclusive.
Return "ERROR" for invalid inputs.

Symbols: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

A smaller symbol placed before a bigger one is subtracted. Only these
subtractions are used: IV (4), IX (9), XL (40), XC (90), CD (400), CM (900).

Your function must be declared as follows:

    def int_to_roman(number: int) -> str:

Examples:
    int_to_roman(3)      -> "III"
    int_to_roman(4)      -> "IV"
    int_to_roman(9)      -> "IX"
    int_to_roman(58)     -> "LVIII"
    int_to_roman(1994)   -> "MCMXCIV"
    int_to_roman(3999)   -> "MMMCMXCIX"
    int_to_roman(0)      -> "ERROR"
    int_to_roman(4000)   -> "ERROR"
""",
        "function": "int_to_roman",
        "tests": [
            ([3], "III"),
            ([4], "IV"),
            ([9], "IX"),
            ([58], "LVIII"),
            ([1994], "MCMXCIV"),
            ([3999], "MMMCMXCIX"),
            ([0], "ERROR"),
            ([4000], "ERROR"),
            ([-5], "ERROR"),
            ([1], "I"),
            ([444], "CDXLIV"),
        ],
    },

    "py_longest_digit_run": {
        "level": 3,
        "subject": """\
Assignment name  : py_longest_digit_run
Expected files   : py_longest_digit_run.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that returns the length of the longest run of the same digit
repeated consecutively in a string.

A run is a sequence of adjacent characters that are all the same digit.
Any non-digit character breaks a run.
Return 0 if the string has no digits.

Your function must be declared as follows:

    def longest_digit_run(text: str) -> int:

Examples:
    longest_digit_run("1112233")     -> 3
    longest_digit_run("a1111b22")    -> 4
    longest_digit_run("12345")       -> 1
    longest_digit_run("77a77")       -> 2
    longest_digit_run("999.99")      -> 3
    longest_digit_run("abc")         -> 0
    longest_digit_run("")            -> 0
""",
        "function": "longest_digit_run",
        "tests": [
            (["1112233"], 3),
            (["a1111b22"], 4),
            (["12345"], 1),
            (["77a77"], 2),
            (["999.99"], 3),
            (["abc"], 0),
            ([""], 0),
            (["5"], 1),
            (["aaa111"], 3),
            (["00 000"], 3),
        ],
    },

    "py_count_occurrences": {
        "level": 3,
        "subject": """\
Assignment name  : py_count_occurrences
Expected files   : py_count_occurrences.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that counts how many times the string 'sub' appears inside
the string 'text', without overlapping.
The search goes from left to right: after an occurrence is found, the search
continues right after the end of that occurrence.
Function is case-sensitive. The method str.count() is not allowed.
If 'sub' is empty, return 0.

Your function must be declared as follows:

    def count_occurrences(sub: str, text: str) -> int:

Examples:
    count_occurrences("ab", "ababab")     -> 3
    count_occurrences("aa", "aaaa")       -> 2
    count_occurrences("aa", "aaa")        -> 1
    count_occurrences("Ab", "abAb")       -> 1
    count_occurrences("x", "abc")         -> 0
    count_occurrences("abc", "ab")        -> 0
    count_occurrences("", "abc")          -> 0
""",
        "function": "count_occurrences",
        "tests": [
            (["ab", "ababab"], 3),
            (["aa", "aaaa"], 2),
            (["aa", "aaa"], 1),
            (["Ab", "abAb"], 1),
            (["x", "abc"], 0),
            (["abc", "ab"], 0),
            (["", "abc"], 0),
            (["", ""], 0),
            (["is", "this is his list"], 4),
            (["aba", "abababa"], 2),
        ],
    },

    # ── LEVEL 4 ──────────────────────────────────────────────
    "py_group_anagrams": {
        "level": 4,
        "subject": """\
Assignment name  : py_group_anagrams
Expected files   : py_group_anagrams.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that groups the words of a list that are anagrams of each
other, ignoring case.

Two words are anagrams if they contain exactly the same letters with the same
quantity.

The groups must be in the order their first word appears in the input list.
Inside each group, words keep the same order as in the input list.

Your function must be declared as follows:

    def group_anagrams(words: list[str]) -> list[list[str]]:

Examples:
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    group_anagrams(["Listen", "silent", "enlist", "abc"])
        -> [["Listen", "silent", "enlist"], ["abc"]]
    group_anagrams(["abc", "def"])
        -> [["abc"], ["def"]]
    group_anagrams(["a"])
        -> [["a"]]
    group_anagrams([])
        -> []
""",
        "function": "group_anagrams",
        "tests": [
            ([["eat", "tea", "tan", "ate", "nat", "bat"]], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
            ([["Listen", "silent", "enlist", "abc"]], [["Listen", "silent", "enlist"], ["abc"]]),
            ([["abc", "def"]], [["abc"], ["def"]]),
            ([["a"]], [["a"]]),
            ([[]], []),
            ([["", ""]], [["", ""]]),
            ([["ab", "ba", "aab", "aba"]], [["ab", "ba"], ["aab", "aba"]]),
            ([["Dog", "god", "GOD"]], [["Dog", "god", "GOD"]]),
        ],
    },

    "py_ransom_note": {
        "level": 4,
        "subject": """\
Assignment name  : py_ransom_note
Expected files   : py_ransom_note.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that checks if the string 'note' can be built using the
characters of the string 'letters'.
Each character of 'letters' can only be used once.
Case sensitive. Spaces in 'note' are ignored (they don't need a letter).
An empty note can always be built.

Your function must be declared as follows:

    def ransom_note(note: str, letters: str) -> bool:

Examples:
    ransom_note("aa", "aab")                   -> True
    ransom_note("aa", "ab")                    -> False
    ransom_note("hello world", "dlrowolleh")   -> True
    ransom_note("Hi", "hi")                    -> False
    ransom_note("", "abc")                     -> True
    ransom_note("abc", "")                     -> False
""",
        "function": "ransom_note",
        "tests": [
            (["aa", "aab"], True),
            (["aa", "ab"], False),
            (["hello world", "dlrowolleh"], True),
            (["Hi", "hi"], False),
            (["", "abc"], True),
            (["abc", ""], False),
            (["", ""], True),
            (["a b c", "cba"], True),
            (["give me 42", "4emigve2"], True),
            (["zzz", "zz"], False),
        ],
    },

    "py_first_unique_char": {
        "level": 4,
        "subject": """\
Assignment name  : py_first_unique_char
Expected files   : py_first_unique_char.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that returns the index of the first character of a string
that appears only once in that string.
Case sensitive: 'a' and 'A' are different characters.
Return -1 if every character is repeated or if the string is empty.

Your function must be declared as follows:

    def first_unique_char(s: str) -> int:

Examples:
    first_unique_char("leetcode")       -> 0
    first_unique_char("loveleetcode")   -> 2
    first_unique_char("aabb")           -> -1
    first_unique_char("aA")             -> 0
    first_unique_char("z")              -> 0
    first_unique_char("")               -> -1
""",
        "function": "first_unique_char",
        "tests": [
            (["leetcode"], 0),
            (["loveleetcode"], 2),
            (["aabb"], -1),
            (["aA"], 0),
            (["z"], 0),
            ([""], -1),
            (["aabbc"], 4),
            (["abcabd"], 2),
            (["  x"], 2),
        ],
    },

    # ── LEVEL 5 ──────────────────────────────────────────────
    "py_snake_to_camel": {
        "level": 5,
        "subject": """\
Assignment name  : py_snake_to_camel
Expected files   : py_snake_to_camel.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that converts a string written in snake_case into camelCase.

Rules:
- Words are separated by one or more underscores '_'
- Underscores at the beginning or at the end of the string are ignored
- The first word is written entirely in lowercase
- Every following word starts with an uppercase letter, and the rest of the
  word is lowercase
- Digits stay unchanged

Your function must be declared as follows:

    def snake_to_camel(text: str) -> str:

Examples:
    snake_to_camel("hello_world")    -> "helloWorld"
    snake_to_camel("make_it_work")   -> "makeItWork"
    snake_to_camel("HELLO_WORLD")    -> "helloWorld"
    snake_to_camel("user__id_2")     -> "userId2"
    snake_to_camel("__init__")       -> "init"
    snake_to_camel("already")        -> "already"
    snake_to_camel("")               -> ""
""",
        "function": "snake_to_camel",
        "tests": [
            (["hello_world"], "helloWorld"),
            (["make_it_work"], "makeItWork"),
            (["HELLO_WORLD"], "helloWorld"),
            (["user__id_2"], "userId2"),
            (["__init__"], "init"),
            (["already"], "already"),
            ([""], ""),
            (["___"], ""),
            (["a_b_c"], "aBC"),
            (["version_2_final"], "version2Final"),
        ],
    },

    "py_reverse_words": {
        "level": 5,
        "subject": """\
Assignment name  : py_reverse_words
Expected files   : py_reverse_words.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that reverses the order of the words in a string.
Words are separated by one or more spaces.
The result must have exactly one space between words, and no spaces at the
beginning or at the end.
The letters inside each word are NOT reversed.

Your function must be declared as follows:

    def reverse_words(text: str) -> str:

Examples:
    reverse_words("hello world")              -> "world hello"
    reverse_words("  the sky   is blue ")     -> "blue is sky the"
    reverse_words("a b c")                    -> "c b a"
    reverse_words("one")                      -> "one"
    reverse_words("   ")                      -> ""
    reverse_words("")                         -> ""
""",
        "function": "reverse_words",
        "tests": [
            (["hello world"], "world hello"),
            (["  the sky   is blue "], "blue is sky the"),
            (["a b c"], "c b a"),
            (["one"], "one"),
            (["   "], ""),
            ([""], ""),
            (["42 is the answer"], "answer the is 42"),
            (["Hello, World!"], "World! Hello,"),
        ],
    },

    # ── LEVEL 6 ──────────────────────────────────────────────
    "py_max_nesting_depth": {
        "level": 6,
        "subject": """\
Assignment name  : py_max_nesting_depth
Expected files   : py_max_nesting_depth.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that returns the maximum nesting depth of the parentheses in
a string.

The depth increases by one for each '(' that is still open.
Only the characters '(' and ')' matter, every other character is ignored.
If the parentheses are not balanced (a ')' without a matching '(' before it,
or a '(' that is never closed), return -1.
A string without parentheses has a depth of 0.

Your function must be declared as follows:

    def max_nesting_depth(s: str) -> int:

Examples:
    max_nesting_depth("(a(b)c)")                -> 2
    max_nesting_depth("()()")                   -> 1
    max_nesting_depth("((()))")                 -> 3
    max_nesting_depth("(1+(2*3)+((8)/4))+1")    -> 3
    max_nesting_depth("abc")                    -> 0
    max_nesting_depth("(()")                    -> -1
    max_nesting_depth(")(")                     -> -1
    max_nesting_depth("")                       -> 0
""",
        "function": "max_nesting_depth",
        "tests": [
            (["(a(b)c)"], 2),
            (["()()"], 1),
            (["((()))"], 3),
            (["(1+(2*3)+((8)/4))+1"], 3),
            (["abc"], 0),
            (["(()"], -1),
            ([")("], -1),
            ([""], 0),
            (["())"], -1),
            (["[{()}]"], 1),
        ],
    },

    "py_atbash_cipher": {
        "level": 6,
        "subject": """\
Assignment name  : py_atbash_cipher
Expected files   : py_atbash_cipher.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that encodes a string with the Atbash cipher.
Each letter is replaced by the letter at the same position counting from the
end of the alphabet: 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.
Uppercase letters stay uppercase and lowercase letters stay lowercase.
Non-alphabetic characters should remain unchanged.

Your function must be declared as follows:

    def atbash_cipher(text: str) -> str:

Examples:
    atbash_cipher("abc")             -> "zyx"
    atbash_cipher("Hello World!")    -> "Svool Dliow!"
    atbash_cipher("xyz123")          -> "cba123"
    atbash_cipher("Zz")              -> "Aa"
    atbash_cipher("")                -> ""
""",
        "function": "atbash_cipher",
        "tests": [
            (["abc"], "zyx"),
            (["Hello World!"], "Svool Dliow!"),
            (["xyz123"], "cba123"),
            (["Zz"], "Aa"),
            ([""], ""),
            (["Svool Dliow!"], "Hello World!"),
            (["42 Porto"], "42 Kligl"),
            (["mM nN"], "nN mM"),
        ],
    },

    "py_run_length_encode": {
        "level": 6,
        "subject": """\
Assignment name  : py_run_length_encode
Expected files   : py_run_length_encode.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that compresses a string using run-length encoding.
Each group of identical consecutive characters is replaced by the character
followed by the number of times it is repeated.
Case sensitive: 'a' and 'A' are different characters.
Spaces and symbols are encoded like any other character.

Your function must be declared as follows:

    def run_length_encode(text: str) -> str:

Examples:
    run_length_encode("aaabcc")          -> "a3b1c2"
    run_length_encode("a")               -> "a1"
    run_length_encode("aAa")             -> "a1A1a1"
    run_length_encode("zzzzzzzzzzzz")    -> "z12"
    run_length_encode("aa  b")           -> "a2 2b1"
    run_length_encode("")                -> ""
""",
        "function": "run_length_encode",
        "tests": [
            (["aaabcc"], "a3b1c2"),
            (["a"], "a1"),
            (["aAa"], "a1A1a1"),
            (["zzzzzzzzzzzz"], "z12"),
            (["aa  b"], "a2 2b1"),
            ([""], ""),
            (["abc"], "a1b1c1"),
            (["!!!??"], "!3?2"),
            (["aabbaa"], "a2b2a2"),
        ],
    },
}