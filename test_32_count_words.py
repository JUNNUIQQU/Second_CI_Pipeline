import importlib

module = importlib.import_module("32_count_words")


def test_count_words():
    assert module.count_words(
        "Python is an easy programming language"
    ) == 6


def test_empty_sentence():
    assert module.count_words("") == 0


def test_single_word():
    assert module.count_words("Python") == 1
    