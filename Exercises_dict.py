# ─────────────────────────────────────────────────────────────
# EXERCISE BANK
# ─────────────────────────────────────────────────────────────
EXERCISES = {
    # ── LEVEL 1 ──────────────────────────────────────────────
    "py_bracket_validator": {
        "level": 6,
        "subject": """\
Assignment name  : py_bracket_validator
Expected files   : py_bracket_validator.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that checks if the brackets in a string are valid.

A string is valid if every opening bracket has a matching closing bracket
in the correct order.

Allowed brackets: (), [], {}

Your function must be declared as follows:

    def bracket_validator(s: str) -> bool:

Examples:
    bracket_validator("()")           -> True
    bracket_validator("()[]{}")       -> True
    bracket_validator("(]")           -> False
    bracket_validator("([)]")         -> False
    bracket_validator("{[]}")         -> True
    bracket_validator("hello(world)") -> True
    bracket_validator("((())")        -> False
    bracket_validator("")             -> True
""",
        "function": "bracket_validator",
        "tests": [
            (["()"],           True),
            (["()[]{}"],       True),
            (["(]"],           False),
            (["([)]"],         False),
            (["{[]}"],         True),
            (["hello(world)[test]{code}"], True),
            (["((()))"],       True),
            (["((())"],        False),
            ([""],             True),
            (["["],            False),
            (["}{"],           False),
        ],
    },

    "py_cryptic_sorter": {
        "level": 1,
        "subject": """\
Assignment name  : py_cryptic_sorter
Expected files   : py_cryptic_sorter.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that sorts a list of strings according to multiple criteria:
1. Primary sort: By string length (shortest first)
2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
4. Equal strings will appear in the same order as in the input list.

Your function must be declared as follows:

    def cryptic_sorter(strings: list[str]) -> list[str]:

The function should return the sorted list.

Your function must handle:
  - Empty strings and empty lists
  - Mixed case strings (treat as lowercase for sorting)
  - Special characters (ignore for vowel counting)

Examples:
    cryptic_sorter(["apple","cat","banana","dog","elephant"])
        -> ["cat","dog","apple","banana","elephant"]
    cryptic_sorter(["aaa","bbb","AAA","BBB"])
        -> ["AAA", "aaa", "BBB", "bbb"]
    cryptic_sorter(["hello","world","hi","test"])
        -> ["hi","test","hello","world"]
    cryptic_sorter([])       -> []
    cryptic_sorter([""])     -> [""]
""",
        "function": "cryptic_sorter",
        "tests": [
            ([["apple","cat","banana","dog","elephant"]], ["cat","dog","apple","banana","elephant"]),
            ([["aaa","bbb","AAA","BBB"]],                  ["AAA", "aaa", "BBB", "bbb"]),
            ([["hello","world","hi","test"]],              ["hi","test","hello","world"]),
            ([[]], []),
            ([[""]],  [""]),
            ([["z","a","m"]],                              ["a","m","z"]),
        ],
    },

    # ── LEVEL 2 ──────────────────────────────────────────────
    "py_echo_validator": {
        "level": 2,
        "subject": """\
Assignment name  : py_echo_validator
Expected files   : py_echo_validator.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that checks if a string is a palindrome,
ignoring spaces and case.

Your function must be declared as follows:

    def echo_validator(text: str) -> bool:

Examples:
    echo_validator("racecar")                    -> True
    echo_validator("A man a plan a canal Panama")-> True
    echo_validator("race a car")                 -> False
    echo_validator("Was it a car or a cat I saw")-> True
    echo_validator("hello")                      -> False
    echo_validator("Madam Im Adam")              -> True
    echo_validator("")                           -> False
""",
        "function": "echo_validator",
        "tests": [
            (["racecar"],                      True),
            (["A man a plan a canal Panama"],  True),
            (["race a car"],                   False),
            (["Was it a car or a cat I saw"],  True),
            (["hello"],                        False),
            (["Madam Im Adam"],                True),
            ([""],                             False),
            (["a"],                            True),
            (["ab"],                           False),
        ],
    },

    "py_mirror_matrix": {
        "level": 2,
        "subject": """\
Assignment name  : py_mirror_matrix
Expected files   : py_mirror_matrix.py
Allowed functions: None
--------------------------------------------------------------------------------

Given a 2D matrix (list of lists), return a new matrix where each row
is reversed.

Your function must be declared as follows:

    def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:

Examples:
    mirror_matrix([[1,2,3],[4,5,6]])      -> [[3,2,1],[6,5,4]]
    mirror_matrix([[1,2],[3,4],[5,6]])    -> [[2,1],[4,3],[6,5]]
    mirror_matrix([[7]])                  -> [[7]]
    mirror_matrix([[1,2,3,4]])            -> [[4,3,2,1]]
    mirror_matrix([[-1,-2],[-3,-4]])      -> [[-2,-1],[-4,-3]]
""",
        "function": "mirror_matrix",
        "tests": [
            ([[[1,2,3],[4,5,6]]],      [[3,2,1],[6,5,4]]),
            ([[[1,2],[3,4],[5,6]]],    [[2,1],[4,3],[6,5]]),
            ([[[7]]],                  [[7]]),
            ([[[1,2,3,4]]],            [[4,3,2,1]]),
            ([[[-1,-2],[-3,-4]]],      [[-2,-1],[-4,-3]]),
        ],
    },

    # ── LEVEL 3 ──────────────────────────────────────────────
    "py_inter": {
        "level": 1,
        "subject": """\
Assignment name  : py_inter
Expected files   : py_inter.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that returns a string with the characters that appear
in both strings, without repetitions. Characters are added in the order
they appear in the first string.

Your function must be declared as follows:

    def inter(s1: str, s2: str) -> str:

Examples:
    inter("hello", "world")   -> "lo"
    inter("banana", "band")   -> "ban"
    inter("abcabc", "bc")     -> "bc"
    inter("abc", "xyz")       -> ""
    inter("", "abc")          -> ""
""",
        "function": "inter",
        "tests": [
            (["hello", "world"],   "lo"),
            (["banana", "band"],   "ban"),
            (["abcabc", "bc"],     "bc"),
            (["abc", "xyz"],       ""),
            (["", "abc"],          ""),
            (["abc", ""],          ""),
            (["aabbcc", "abc"],    "abc"),
        ],
    },

    "py_number_base_converter": {
        "level": 3,
        "subject": """\
Assignment name  : py_number_base_converter
Expected files   : py_number_base_converter.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that converts a number from one base to another.
Support bases from 2 to 36 inclusive.
Use digits 0-9 and letters A-Z for values 10-35.
Return "ERROR" for invalid inputs.

Your function must be declared as follows:

    def number_base_converter(number: str, from_base: int, to_base: int) -> str:

Examples:
    number_base_converter("1010", 2, 10)  -> "10"
    number_base_converter("FF", 16, 10)   -> "255"
    number_base_converter("255", 10, 16)  -> "FF"
    number_base_converter("123", 10, 2)   -> "1111011"
    number_base_converter("Z", 36, 10)    -> "35"
    number_base_converter("35", 10, 36)   -> "Z"
    number_base_converter("123", 1, 10)   -> "ERROR"
    number_base_converter("G", 16, 10)    -> "ERROR"
""",
        "function": "number_base_converter",
        "tests": [
            (["1010", 2, 10],   "10"),
            (["FF", 16, 10],    "255"),
            (["255", 10, 16],   "FF"),
            (["123", 10, 2],    "1111011"),
            (["Z", 36, 10],     "35"),
            (["35", 10, 36],    "Z"),
            (["123", 1, 10],    "ERROR"),
            (["G", 16, 10],     "ERROR"),
            (["0", 10, 2],      "0"),
            (["1", 2, 10],      "1"),
        ],
    },

    "py_pattern_tracker": {
        "level": 3,
        "subject": """\
Assignment name  : py_pattern_tracker
Expected files   : py_pattern_tracker.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that counts the number of valid consecutive digit pairs
in a string. A valid pair consists of two adjacent digits where the second
digit is exactly one greater than the first.
A 9 followed by a 0 is NOT a valid pair.

Your function must be declared as follows:

    def pattern_tracker(text: str) -> int:

Examples:
    pattern_tracker("123")        -> 2
    pattern_tracker("12a34")      -> 2
    pattern_tracker("987654321")  -> 0
    pattern_tracker("01234567")   -> 7
    pattern_tracker("abc")        -> 0
    pattern_tracker("1a2b3c4")    -> 0
    pattern_tracker("112233")     -> 2
""",
        "function": "pattern_tracker",
        "tests": [
            (["123"],       2),
            (["12a34"],     2),
            (["987654321"], 0),
            (["01234567"],  7),
            (["abc"],       0),
            (["1a2b3c4"],   0),
            (["112233"],    2),
            (["90"],        0),
            ([""],          0),
        ],
    },

    # ── LEVEL 4 ──────────────────────────────────────────────
    "py_anagram": {
        "level": 4,
        "subject": """\
Assignment name  : py_anagram
Expected files   : py_anagram.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that checks if two strings are anagrams.
They must contain exactly the same letters with the same quantity,
ignoring case and spaces.

Your function must be declared as follows:

    def anagram(s1: str, s2: str) -> bool:

Examples:
    anagram("listen", "silent")             -> True
    anagram("Triangle", "Integral")         -> True
    anagram("Dormitory", "Dirty Room")      -> True
    anagram("hello", "world")               -> False
    anagram("", "")                         -> True
    anagram("abc", "abcc")                  -> False
""",
        "function": "anagram",
        "tests": [
            (["listen", "silent"],              True),
            (["Triangle", "Integral"],          True),
            (["Dormitory", "Dirty Room"],       True),
            (["Astronomer", "Moon starer"],     True),
            (["hello", "world"],                False),
            (["test", "ttew"],                  False),
            (["abc", "abcc"],                   False),
            (["", ""],                          True),
            (["a gentleman", "elegant man"],    True),
            (["aabb", "ab"],                    False),
        ],
    },

    "py_shadow_merge": {
        "level": 4,
        "subject": """\
Assignment name  : py_shadow_merge
Expected files   : py_shadow_merge.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that merges two sorted lists into one sorted list.

Your function must be declared as follows:

    def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:

Examples:
    shadow_merge([1,3,5], [2,4,6])    -> [1,2,3,4,5,6]
    shadow_merge([1,2,3], [4,5,6])    -> [1,2,3,4,5,6]
    shadow_merge([1], [2,3,4])        -> [1,2,3,4]
    shadow_merge([], [1,2,3])         -> [1,2,3]
    shadow_merge([1,1,2], [1,3,3])    -> [1,1,1,2,3,3]
""",
        "function": "shadow_merge",
        "tests": [
            ([[1,3,5], [2,4,6]],     [1,2,3,4,5,6]),
            ([[1,2,3], [4,5,6]],     [1,2,3,4,5,6]),
            ([[1], [2,3,4]],         [1,2,3,4]),
            ([[], [1,2,3]],          [1,2,3]),
            ([[1,1,2], [1,3,3]],     [1,1,1,2,3,3]),
            ([[],[]],                []),
            ([[5],[5]],              [5,5]),
        ],
    },

    "py_string_permutation_checker": {
        "level": 4,
        "subject": """\
Assignment name  : py_string_permutation_checker
Expected files   : py_string_permutation_checker.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that determines if two strings are permutations of each other.
Case sensitive. Whitespace and punctuation count as regular characters.
Empty strings are permutations of each other.

Your function must be declared as follows:

    def string_permutation_checker(s1: str, s2: str) -> bool:

Examples:
    string_permutation_checker("abc", "bca")              -> True
    string_permutation_checker("abc", "def")              -> False
    string_permutation_checker("listen", "silent")        -> True
    string_permutation_checker("hello", "bello")          -> False
    string_permutation_checker("", "")                    -> True
    string_permutation_checker("a", "")                   -> False
    string_permutation_checker("Abc", "abc")              -> False
    string_permutation_checker("a gentleman","elegant man")-> True
""",
        "function": "string_permutation_checker",
        "tests": [
            (["abc", "bca"],                True),
            (["abc", "def"],                False),
            (["listen", "silent"],          True),
            (["hello", "bello"],            False),
            (["", ""],                      True),
            (["a", ""],                     False),
            (["Abc", "abc"],                False),
            (["a gentleman","elegant man"], True),
        ],
    },

    # ── LEVEL 5 ──────────────────────────────────────────────
    "py_string_sculptor": {
        "level": 5,
        "subject": """\
Assignment name  : py_string_sculptor
Expected files   : py_string_sculptor.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that transforms a string by alternating the case of
alphabetic characters only.
Non-alphabetic characters remain unchanged and are NOT counted in the
alternation index.
The first alphabetic character should be lowercase, the second uppercase, etc.
Spaces reset the alternation (next alpha after a space is lowercase again).

Your function must be declared as follows:

    def string_sculptor(text: str) -> str:

Examples:
    string_sculptor("hello")        -> "hElLo"
    string_sculptor("Hello World")  -> "hElLo wOrLd"
    string_sculptor("abc123def")    -> "aBc123DeF"
    string_sculptor("Python3.9!")   -> "pYtHoN3.9!"
    string_sculptor("")             -> ""
""",
        "function": "string_sculptor",
        "tests": [
            (["hello"],        "hElLo"),
            (["Hello World"],  "hElLo wOrLd"),
            (["abc123def"],    "aBc123DeF"),
            (["Python3.9!"],   "pYtHoN3.9!"),
            ([""],             ""),
            (["a"],            "a"),
            (["AB"],           "aB"),
        ],
    },

    "py_twist_sequence": {
        "level": 5,
        "subject": """\
Assignment name  : py_twist_sequence
Expected files   : py_twist_sequence.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that rotates an array to the right by k positions.
Rotating right by k means the last k elements move to the front.

Your function must be declared as follows:

    def twist_sequence(arr: list[int], k: int) -> list[int]:

Examples:
    twist_sequence([1,2,3,4,5], 2)  -> [4,5,1,2,3]
    twist_sequence([1,2,3], 1)      -> [3,1,2]
    twist_sequence([1,2,3,4], 0)    -> [1,2,3,4]
    twist_sequence([1,2,3], 5)      -> [2,3,1]
    twist_sequence([], 3)           -> []
""",
        "function": "twist_sequence",
        "tests": [
            ([[1,2,3,4,5], 2],  [4,5,1,2,3]),
            ([[1,2,3], 1],      [3,1,2]),
            ([[1,2,3,4], 0],    [1,2,3,4]),
            ([[1,2,3], 5],      [2,3,1]),
            ([[], 3],           []),
            ([[1], 1],          [1]),
            ([[1,2], 4],        [1,2]),
        ],
    },

    # ── LEVEL 6 ──────────────────────────────────────────────
    "py_whisper_cipher": {
        "level": 6,
        "subject": """\
Assignment name  : py_whisper_cipher
Expected files   : py_whisper_cipher.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that creates a Caesar cipher by shifting letters in a
string by a given amount.
Non-alphabetic characters should remain unchanged.
The shift can be negative (shift left).

Your function must be declared as follows:

    def whisper_cipher(text: str, shift: int) -> str:

Examples:
    whisper_cipher("hello", 3)       -> "khoor"
    whisper_cipher("Hello World!", 1)-> "Ifmmp Xpsme!"
    whisper_cipher("xyz", 3)         -> "abc"
    whisper_cipher("ABC123def", 5)   -> "FGH123ijk"
    whisper_cipher("", 10)           -> ""
    whisper_cipher("abc", -3)        -> "xyz"
""",
        "function": "whisper_cipher",
        "tests": [
            (["hello", 3],        "khoor"),
            (["Hello World!", 1], "Ifmmp Xpsme!"),
            (["xyz", 3],          "abc"),
            (["ABC123def", 5],    "FGH123ijk"),
            (["", 10],            ""),
            (["abc", -3],         "xyz"),
            (["abc", 0],          "abc"),
            (["abc", 26],         "abc"),
        ],
    },

    # ── BONUS: hidenp ─────────────────────────────────────────
    "py_hidenp": {
        "level": 3,
        "subject": """\
Assignment name  : py_hidenp
Expected files   : py_hidenp.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that checks if the string 'small' is a subsequence
of 'big'. A subsequence means all characters of 'small' appear in 'big'
in the same order, but not necessarily consecutively.
Function is case-sensitive.

Your function must be declared as follows:

    def hidenp(small: str, big: str) -> bool:

Examples:
    hidenp("abc", "a1b2c3")              -> True
    hidenp("ace", "abcde")               -> True
    hidenp("aec", "abcde")               -> False
    hidenp("", "abc")                    -> True
    hidenp("abc", "ab")                  -> False
    hidenp("aaaa", "aaa")                -> False
    hidenp("sing","subsequence testing") -> True
""",
        "function": "hidenp",
        "tests": [
            (["abc", "a1b2c3"],              True),
            (["ace", "abcde"],               True),
            (["aec", "abcde"],               False),
            (["", "abc"],                    True),
            (["", ""],                       True),
            (["abc", "ab"],                  False),
            (["xyz", "abc"],                 False),
            (["aaaa", "aaa"],                False),
            (["aab", "aaab"],                True),
            (["aba", "aabb"],                False),
            (["abc", "ABC"],                 False),
            (["sing","subsequence testing"], True),
        ],
    },
}
