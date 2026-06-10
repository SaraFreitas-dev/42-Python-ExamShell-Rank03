#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║          EXAMSHELL - Exam Rank 03 Common Core        ║
║                  42 School Style                     ║
╚══════════════════════════════════════════════════════╝
Usage: python3 examshell_rank3.py
"""

import os
import sys
import time
import random
import subprocess
import textwrap
import difflib
import tempfile
from datetime import datetime
from Exercises_dict import EXERCISES

# ─────────────────────────────────────────────────────────────
# COLORS
# ─────────────────────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"
    BG_RED  = "\033[41m"
    BG_GREEN= "\033[42m"
    BG_BLUE = "\033[44m"

def c(color, text): return f"{color}{text}{C.RESET}"

# ─────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────
class Session:
    def __init__(self):
        self.start_time: float | None = None
        self.login        = os.environ.get("USER", "student")
        self.current_ex   = None
        self.current_level= None
        self.attempts     = 0
        self.passed       = []
        self.failed_ex    = []
        self.exam_dir = "exam_workspace"
        os.makedirs(self.exam_dir, exist_ok=True)
        self.exam_over    = False

    def elapsed(self):
        if self.start_time is None:
            return "00:00:00"

        s = int(time.time() - self.start_time)
        return f"{s//3600:02d}:{(s%3600)//60:02d}:{s%60:02d}"

    def score(self):
        return int((len(self.passed) / 6) * 100)

# ─────────────────────────────────────────────────────────────
# UI HELPERS
# ─────────────────────────────────────────────────────────────
def clear():
    os.system("clear" if os.name != "nt" else "cls")

def banner():
    print(c(C.CYAN, "╔" + "═"*54 + "╗"))
    print(c(C.CYAN, "║") + c(C.BOLD + C.WHITE, "      EXAMSHELL - Exam Rank 03 Common Core          ") + c(C.CYAN, "  ║"))
    print(c(C.CYAN, "║") + c(C.GRAY, "             42 School  ·  Python Edition             ") + c(C.CYAN, "║"))
    print(c(C.CYAN, "╚" + "═"*54 + "╝"))

def divider(char="─", color=C.GRAY):
    print(c(color, char * 56))

def print_status(session):
    elapsed = session.elapsed()
    score   = session.score()
    level   = session.current_level or "-"
    exname  = session.current_ex   or "-"
    passed  = len(session.passed)
    print()
    divider("═", C.CYAN)
    print(
        c(C.CYAN, "  LOGIN: ") + c(C.WHITE + C.BOLD, session.login.ljust(15)) +
        c(C.CYAN, " LEVEL: ") + c(C.YELLOW, str(level).ljust(3)) +
        c(C.CYAN, " TIME: ") + c(C.WHITE, elapsed)
    )
    print(
        c(C.CYAN, "  SCORE: ") + c(C.GREEN + C.BOLD, f"{score}/100".ljust(10)) +
        c(C.CYAN, " EXERCISES PASSED: ") + c(C.GREEN, str(passed))
    )
    divider("═", C.CYAN)
    print()

def show_subject(ex_name, session):
    ex = EXERCISES[ex_name]
    clear()
    banner()
    print_status(session)
    print(c(C.BOLD + C.YELLOW, f"  📄 EXERCISE: {ex_name}") +
          c(C.GRAY, f"  (Level {ex['level']})"))
    divider()
    lines = ex["subject"].splitlines()
    for line in lines:
        if line.startswith("Assignment") or line.startswith("Expected") or line.startswith("Allowed"):
            print(c(C.CYAN, "  " + line))
        elif line.startswith("----"):
            print(c(C.GRAY, "  " + line))
        elif "->" in line:
            idx = line.index("->")
            print("  " + c(C.WHITE, line[:idx]) + c(C.GREEN, "->") + c(C.YELLOW, line[idx+2:]))
        elif line.strip().startswith("def "):
            print("  " + c(C.MAGENTA, line))
        else:
            print("  " + line)
    divider()

# ─────────────────────────────────────────────────────────────
# GRADER
# ─────────────────────────────────────────────────────────────
def grade_submission(ex_name, filepath, session):
    ex      = EXERCISES[ex_name]
    fn_name = ex["function"]
    tests   = ex["tests"]

    results = []
    passed  = 0

    for args, expected in tests:
        test_code = f"""
import sys, os
sys.path.insert(0, os.path.dirname('{filepath}'))
"""
        # build import
        module_name = os.path.splitext(os.path.basename(filepath))[0]
        test_code += f"from {module_name} import {fn_name}\n"
        # build call
        arg_repr = ", ".join(repr(a) for a in args)
        test_code += f"result = {fn_name}({arg_repr})\n"
        test_code += f"print(repr(result))\n"

        try:
            proc = subprocess.run(
                [sys.executable, "-c", test_code],
                capture_output=True, text=True, timeout=5
            )
            if proc.returncode != 0:
                got = f"[RUNTIME ERROR] {proc.stderr.strip()[:80]}"
                ok  = False
            else:
                got_raw = proc.stdout.strip()
                got     = eval(got_raw)
                ok      = (got == expected)
        except subprocess.TimeoutExpired:
            got = "[TIMEOUT]"
            ok  = False
        except Exception as e:
            got = f"[ERROR] {e}"
            ok  = False

        results.append((args, expected, got, ok))
        if ok:
            passed += 1

    return results, passed, len(tests)

def print_grade_report(ex_name, results, passed, total):
    print()
    divider("─", C.CYAN)
    print(c(C.BOLD + C.WHITE, f"  TEST RESULTS FOR: {ex_name}"))
    divider()
    ex = EXERCISES[ex_name]
    fn = ex["function"]
    for i, (args, expected, got, ok) in enumerate(results):
        status = c(C.GREEN, "  ✔ OK  ") if ok else c(C.RED, "  ✘ KO  ")
        arg_str = ", ".join(repr(a) for a in args)
        call    = f"{fn}({arg_str})"
        if len(call) > 45:
            call = call[:42] + "..."
        if ok:
            print(f"{status}{c(C.GRAY, call)}")
        else:
            print(f"{status}{c(C.WHITE, call)}")
            print(f"          {c(C.GRAY,'expected:')} {c(C.GREEN, repr(expected))}")
            print(f"          {c(C.GRAY,'got     :')} {c(C.RED, repr(got))}")
    divider()
    pct = int(passed / total * 100)
    color = C.GREEN if pct == 100 else (C.YELLOW if pct >= 50 else C.RED)
    print(c(C.BOLD + color, f"  {passed}/{total} tests passed  ({pct}%)"))
    divider()

# ─────────────────────────────────────────────────────────────
# ASSIGNMENT PICKER
# ─────────────────────────────────────────────────────────────
def pick_exercise(level, exclude=None):
    """Pick a random exercise from the given level, not in exclude list."""
    pool = [n for n, e in EXERCISES.items() if e["level"] == level]
    if exclude:
        pool = [n for n in pool if n not in exclude]
    if not pool:
        # try any level if this one is exhausted
        pool = [n for n, e in EXERCISES.items() if n not in (exclude or [])]
    if not pool:
        return None
    return random.choice(pool)

# ─────────────────────────────────────────────────────────────
# EXAM FLOW
# ─────────────────────────────────────────────────────────────
def get_assignment(session):
    """Assign the next exercise based on progression."""
    if len(session.passed) == 0:
        level = 1
    elif len(session.passed) == 1:
        level = 2
    elif len(session.passed) == 2:
        level = 3
    elif len(session.passed) == 3:
        level = 4
    else:
        level = 5 + (len(session.passed) - 4)
        level = min(level, 6)

    ex_name = pick_exercise(level, exclude=session.passed + session.failed_ex)
    if ex_name is None:
        ex_name = pick_exercise(level, exclude=session.passed)
    session.current_ex    = ex_name
    session.current_level = level
    return ex_name

def run_exam(session):
    """Main exam loop."""
    while True:
        # ── check time limit (3 hours)
        if session.start_time and time.time() - session.start_time > 3 * 3600:
            clear()
            banner()
            print(c(C.RED + C.BOLD, "\n  ⏰  TIME'S UP — Exam ended (3h limit)"))
            break

        ex_name = get_assignment(session)
        if ex_name is None:
            print(c(C.GREEN, "\n  🎉  All exercises completed!"))
            break

        # Show subject
        show_subject(ex_name, session)
        expected_file = ex_name + ".py"
        work_path     = os.path.join(session.exam_dir, expected_file)

        print(c(C.YELLOW, f"\n  📁  Work dir : {session.exam_dir}"))
        print(c(C.WHITE,  f"  📝  Create   : {expected_file}"))
        print()
        print(c(C.GRAY,   "  Commands:"))
        print(c(C.CYAN,   "    [Enter]    - Compile & test your file"))
        print(c(C.CYAN,   "    subject    - Re-read the subject"))
        print(c(C.CYAN,   "    status     - Show current score"))
        print(c(C.CYAN,   "    next       - Skip this exercise (penalty: no retry)"))
        print(c(C.CYAN,   "    quit/exit  - Exit the exam"))
        print()

        # ── inner loop for this exercise
        while True:
            try:
                cmd = input(c(C.BOLD + C.GREEN, f"  examshell> ")).strip().lower()
            except (KeyboardInterrupt, EOFError):
                print(c(C.YELLOW, "\n\n  Use 'quit' to exit the exam."))
                continue

            if cmd in ("quit", "exit", "q"):
                session.exam_over = True
                break

            if cmd == "subject":
                show_subject(ex_name, session)
                continue

            if cmd == "status":
                print_status(session)
                continue

            if cmd == "next":
                print(c(C.YELLOW, f"\n  ⚠  Skipping {ex_name} — it won't appear again."))
                session.failed_ex.append(ex_name)
                time.sleep(1)
                break

            if cmd == "" or cmd == "grademe":
                # Check file exists
                if not os.path.isfile(work_path):
                    print(c(C.RED, f"\n  ✘  File not found: {work_path}"))
                    print(c(C.GRAY, f"     Create the file and try again.\n"))
                    continue

                print(c(C.CYAN, f"\n  ⚙  Grading {expected_file} ..."))
                session.attempts += 1
                results, passed_n, total_n = grade_submission(ex_name, work_path, session)
                print_grade_report(ex_name, results, passed_n, total_n)

                if passed_n == total_n:
                    print(c(C.GREEN + C.BOLD, "\n  🏆  PERFECT SCORE — Exercise validated!\n"))
                    session.passed.append(ex_name)

                    if len(session.passed) >= 6:
                        session.exam_over = True
                    time.sleep(1.5)
                    break
                else:
                    remaining = total_n - passed_n
                    print(c(C.YELLOW, f"\n  Fix {remaining} failing test(s) and press [Enter] again.\n"))
                continue
            if session.exam_over:
                break
            print(c(C.GRAY, f"  Unknown command: '{cmd}'  — try [Enter] to grade or 'subject'"))

        if session.exam_over:
            break

    # ── final screen
    clear()
    banner()
    elapsed = session.elapsed()
    score   = session.score()
    passed  = len(session.passed)
    print()
    divider("═", C.CYAN)
    print(c(C.BOLD + C.WHITE, "  EXAM COMPLETE"))
    divider()
    print(c(C.CYAN,  f"  Login   : ") + c(C.WHITE + C.BOLD, session.login))
    print(c(C.CYAN,  f"  Time    : ") + c(C.WHITE, elapsed))
    print(c(C.CYAN,  f"  Attempts: ") + c(C.WHITE, str(session.attempts)))
    print(c(C.CYAN,  f"  Passed  : ") + c(C.GREEN + C.BOLD, f"{passed} exercise(s)"))
    if session.passed:
        for ex in session.passed:
            lvl = EXERCISES[ex]["level"]
            print(c(C.GRAY, f"    ✔ [{lvl}] ") + c(C.WHITE, ex))
    print()
    color = C.GREEN if len(session.passed) >= 6 else C.RED
    print(c(C.BOLD + color,
        f"  FINAL SCORE : {len(session.passed)} / 6 exercises ({score}%)"))
    status_msg = "PASSED ✔" if len(session.passed) >= 6 else "FAILED ✘"
    print(c(C.BOLD + color, f"  STATUS      : {status_msg}"))
    divider("═", C.CYAN)
    print()

# ─────────────────────────────────────────────────────────────
# MENU
# ─────────────────────────────────────────────────────────────
def main_menu():
    clear()
    banner()
    print()
    print(c(C.WHITE,  "  Welcome to ExamShell for Exam Rank 03 Common Core."))
    print(c(C.GRAY,   "  This simulator replicates the 42 School exam environment."))
    print()
    print(c(C.YELLOW, "  RULES:"))
    print(c(C.GRAY,   "   • You have 3 hours total."))
    print(c(C.GRAY,   "   • Exercises are assigned by level (1–6)."))
    print(c(C.GRAY,   "   • Complete 6 exercises to pass."))
    print(c(C.GRAY,   "   • Write your solution in the exam_workspace folder."))
    print(c(C.GRAY,   "   • Press [Enter] to submit and grade."))
    print()
    divider()
    print(c(C.CYAN,  "  [1] Start Exam"))
    print(c(C.CYAN,  "  [2] Practice Mode (choose exercise)"))
    print(c(C.CYAN,  "  [3] List all exercises"))
    print(c(C.CYAN,  "  [q] Quit"))
    divider()
    return input(c(C.BOLD + C.WHITE, "\n  > ")).strip().lower()

def practice_menu(session):
    """Let the user pick any specific exercise."""
    clear()
    banner()
    print()
    print(c(C.BOLD + C.WHITE, "  PRACTICE MODE — Choose an exercise:"))
    print()
    by_level = {}
    for name, ex in EXERCISES.items():
        by_level.setdefault(ex["level"], []).append(name)

    idx = 1
    mapping = {}
    for level in sorted(by_level):
        print(c(C.YELLOW, f"  ── Level {level} " + "─"*40))
        for name in sorted(by_level[level]):
            print(c(C.CYAN, f"  [{idx:2d}] ") + c(C.WHITE, name))
            mapping[str(idx)] = name
            idx += 1
        print()

    choice = input(c(C.BOLD + C.WHITE, "  Pick number (or Enter to go back): ")).strip()
    if choice in mapping:
        session.current_ex    = mapping[choice]
        session.current_level = EXERCISES[mapping[choice]]["level"]
        run_single(mapping[choice], session)

def run_single(ex_name, session):
    """Run one exercise in practice mode."""
    work_path = os.path.join(session.exam_dir, ex_name + ".py")
    show_subject(ex_name, session)
    print(c(C.YELLOW, f"\n  📁  Work dir : {session.exam_dir}"))
    print(c(C.WHITE,  f"  📝  Create   : {ex_name}.py"))
    print(c(C.GRAY,   "\n  Press [Enter] to grade, 'subject' to re-read, 'back' to menu\n"))

    while True:
        try:
            cmd = input(c(C.BOLD + C.MAGENTA, "  practice> ")).strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            break

        if cmd in ("back", "b", "quit", "exit"):
            break
        if cmd == "subject":
            show_subject(ex_name, session)
            continue
        if cmd == "" or cmd == "grademe":
            if not os.path.isfile(work_path):
                print(c(C.RED, f"\n  ✘  File not found: {work_path}\n"))
                continue
            print(c(C.CYAN, f"\n  ⚙  Grading ..."))
            results, pn, tn = grade_submission(ex_name, work_path, session)
            print_grade_report(ex_name, results, pn, tn)
            if pn == tn:
                print(c(C.GREEN + C.BOLD, "\n  🏆  All tests passed!\n"))
            continue
        print(c(C.GRAY, f"  Unknown command."))

def list_exercises():
    clear()
    banner()
    print()
    by_level = {}
    for name, ex in EXERCISES.items():
        by_level.setdefault(ex["level"], []).append(name)
    for level in sorted(by_level):
        print(c(C.YELLOW, f"  ── Level {level} " + "─"*40))
        for name in sorted(by_level[level]):
            fn = EXERCISES[name]["function"]
            print(c(C.CYAN, f"    {name}") + c(C.GRAY, f"  ({fn})"))
        print()
    input(c(C.GRAY, "  [Press Enter to continue]"))

# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────
def main():
    session = Session()
    while True:
        choice = main_menu()
        if choice == "1":
            session = Session()
            clear()
            banner()
            login = input(c(C.BOLD + C.WHITE, "\n  Enter your login: ")).strip()
            if login:
                session.login = login
            session.start_time = time.time()
            print(c(C.CYAN, f"\n  Starting exam for {session.login}..."))
            time.sleep(1)
            run_exam(session)
            input(c(C.GRAY, "\n  [Press Enter to return to menu]"))
        elif choice == "2":
            practice_menu(session)
        elif choice == "3":
            list_exercises()
        elif choice in ("q", "quit", "exit"):
            print(c(C.GRAY, "\n  Goodbye!\n"))
            sys.exit(0)

if __name__ == "__main__":
    main()