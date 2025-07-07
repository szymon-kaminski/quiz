# Quiz App in Python

![CI](https://github.com/szymon-kaminski/quiz/actions/workflows/python-tests.yml/badge.svg)

This is a simple command-line quiz app that reads true/false questions from a CSV file and allows the user to interactively answer them.

### Task Description

Write a program that simulates a quiz, reading a series of true/false questions from a file `questions.csv`.

- Display questions one by one.
- Wait for user input: `true`, `false`, `skip`, or `exit`.
- If the answer is correct → move to next question.
- If the answer is incorrect → continue to next without asking again.
- If the user types `skip` → skip to next question.
- If the user types `exit` → end the quiz immediately.
- At the end, display the number of correct answers.

### Features used

- `match-case` statement
- `break` and `continue` in loops
- reading CSV files

### Files

- `questions.csv` – list of quiz questions
- `quiz.py` – main program logic
- `README.md` – project documentation

### How to run

```bash
python quiz.py
```
