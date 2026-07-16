from project import check_answer, load_questions, run_quiz
import io
import sys


def test_check_answer():
    question = {"text": "sample", "answer": "c"}
    assert check_answer(question, "c") == True
    assert check_answer(question, "C") == True
    assert check_answer(question, "a") == False


def test_load_questions():
    easy = load_questions("easy")
    medium = load_questions("medium")
    hard = load_questions("hard")
    assert len(easy) == 10
    assert len(medium) == 10
    assert len(hard) == 10
    assert easy[0]["answer"] == "c"


def test_run_quiz(monkeypatch):
    questions = load_questions("easy")
    answers = iter([q["answer"] for q in questions])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    score = run_quiz(questions)
    assert score == 10
