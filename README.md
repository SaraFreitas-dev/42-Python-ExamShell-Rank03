<p align="center">
  <img src="assets/banner_practice_rank03.png" alt="PracticeShell Banner" width="800">
</p>

<br>

<h1 align="center">Rank 03 (Python) PracticeShell - Exercises & Solutions</h1>

<br>


> [!WARNING]
> At the request of the 42 Network, this repository no longer contains the real Rank 03 exam subjects or solutions. The PracticeShell now uses **original exercises**. They are great for training, but they are **not** the actual exam questions.


---

# 💡 About

This repository is a **growing bank of exercises** for the topics learned during Milestone 3 of the Python Common Core.

The goal is to help you:

- **Train** the topics you learned during the milestone
- **Review** your doubts and find your weak points
- **Prepare** for the exam by practicing under time and test pressure.

New exercises will be added over time. Each one focuses on a concept learned during this milestone.

---

<br>
<p align="center">
  <img src="assets/terminal_menu.png" alt="PracticeShell Preview" width="400">
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-main-feature-practiceshell-simulator">Features</a> •
  <a href="#-exam-mode">Exam Mode</a> •
  <a href="#-practice-mode">Practice Mode</a> •
  <a href="#-solutions">Solutions</a>
</p>

---

A Python-based **PracticeShell simulator** inspired by the new 42 School Common Core Rank 03 learning material, combined with a collection of organized solutions grouped by difficulty level.

---

# 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/SaraFreitas-dev/42-Python-ExamShell-Rank03
cd 42-Python-ExamShell-Rank03
```

Run the PracticeShell:

```bash
python3 practiceshell.py
```

You will be presented with the main menu:

```text
[1] Start Exam
[2] Practice Mode
[3] List all exercises
[q] Quit
```

No dependencies, no setup: just Python 3.

---

## 📝 Workspace

When the PracticeShell starts, it automatically creates an `exam_workspace` directory.

All exercise files should be created inside this folder. The grader will only validate solutions placed in the generated workspace.

Example:

```text
exam_workspace/
└── py_word_length_sorter.py
```

Simply create the requested file, implement your solution, and submit it through the PracticeShell interface for automatic evaluation.

---

# ⭐ Main Feature: PracticeShell Simulator

The PracticeShell is the core of this repository.

It lets you practice each milestone topic hands-on, with hidden tests and automatic feedback, instead of just reading solutions.

<p align="center">
  <img src="assets/terminal_example.png" alt="PracticeShell Preview" width="400">
</p>

| Grading | Exam experience | Interface |
|---|---|---|
| Automatic grading | Random exercise assignment | Colored terminal UI |
| Hidden test cases | Progressive level system | Score tracking |
| Timeout protection | Exam & practice modes | Time tracking |
| 6 difficulty levels | Rank progression logic | Pure Python |

The workflow:

1. Receive a subject
2. Create the requested Python file
3. Implement the solution
4. Submit for grading
5. Fix failing tests
6. Progress to the next level

<p align="center">
  <img src="assets/ko_grade.png" alt="PracticeShell KO example" width="400">
</p>

---

# 🎯 Exam Mode

Select:

```text
[1] Start Exam
```

The simulator will:

- Assign exercises automatically
- Increase difficulty after each successful exercise
- Track your score
- Simulate a 3-hour exam session

## 🏆 Passing the Exam

The simulator uses a progressive difficulty system.
To successfully complete the exam you must validate:

```text
6 / 6 exercises
```

---

# 🛠 Practice Mode

Select:

```text
[2] Practice Mode
```

Practice Mode allows you to:

- Choose any exercise
- Focus on a specific level
- Submit unlimited times
- Train without time pressure

---

# 📚 Solutions

Solutions are organized by level and include the completed exercises.

```text
solutions/
├── level_1
├── level_2
├── level_3
├── level_4
├── level_5
└── level_6
```

This makes it easy to study specific difficulty ranges or review previously solved exercises.

> ⚠️ Try each exercise in the PracticeShell first. Reading solutions before attempting them will not show you where your weak points are.

---

# 📖 Topics Covered

- Strings and string transformations
- Lists and matrices
- Dictionaries and character counting
- Sorting with custom criteria
- Palindromes and anagrams
- Ciphers and character shifting
- Number conversion (Roman numerals, binary)
- Rotation and merging of lists
- Stacks and balanced structures
- Edge case handling
- Algorithmic thinking

---

## ⚠️ Disclaimer

This project is an independent educational tool.
It is not affiliated with or endorsed by 42 School, and it does not contain any official 42 exam content.

---

## 💡 Suggestions

Found a bug, a missing test case or have an idea? Feel free to [open an issue](https://github.com/SaraFreitas-dev/42-Python-ExamShell-Rank03/issues).

---

## ⭐ Support

<h3 align="center">If this repository helped you prepare for the exam, consider giving it a star ⭐</h3>

<p align="center">Good luck and happy coding 🚀</p>