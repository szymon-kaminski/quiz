import builtins
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quiz import run_quiz
from quiz import read_questions

def test_read_questions_returns_expected_output():
    test_file = "tests/test_questions.csv"
    expected = [
        ("Is Python a programming language?", True),
        ("Is the sky green?", False)
    ]
    result = read_questions(test_file)
    assert result == expected


def test_read_questions_should_fail():
    test_file = "tests/test_questions.csv"
    wrong_expected = [
        ("Is Python a snake?", False),  # <--- celowo zła odpowiedź
        ("Is the sky green?", True)     # <--- celowo zła odpowiedź
    ]
    result = read_questions(test_file)
    assert result == wrong_expected


def test_run_quiz_with_mock_input(monkeypatch, capsys):
    questions = [
        ("Python is a programing language.", True),
        ("The Sun is cold.", False),
    ]

    user_inputs = iter(["true", "false"])
    monkeypatch.setattr(builtins, "input", lambda _: next(user_inputs))

    run_quiz(questions)

    output = capsys.readouterr().out

    assert "Your Score: 2 / 2" in output