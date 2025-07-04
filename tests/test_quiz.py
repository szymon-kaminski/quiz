import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quiz import read_questions

def test_read_questions_returns_expected_output():
    test_file = "tests/test_questions.csv"
    expected = [
        ("Is Python a programming language?", True),
        ("Is the sky green?", False)
    ]
    result = read_questions(test_file)
    assert result == expected
