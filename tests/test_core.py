import pytest
from pydog.core import speak, bark, wag


# ---- SPEAK TESTS ----
def test_speak_returns_string():
    result = speak("hello", "happy")
    assert isinstance(result, str)


def test_speak_contains_message():
    result = speak("hello", "happy")
    assert "hello" in result


def test_speak_changes_with_mood():
    happy = speak("hi", "happy")
    angry = speak("hi", "angry")
    assert happy != angry


def test_speak_case_insensitive_mood():
    result = speak("hi", "HAPPY")
    assert "hi" in result


def test_speak_strips_whitespace():
    result = speak("  hi  ", " happy ")
    assert "hi" in result


def test_speak_invalid_mood():
    with pytest.raises(ValueError):
        speak("hello", "sad")


def test_speak_empty_message():
    with pytest.raises(ValueError):
        speak("   ", "happy")


# ---- BARK TESTS ----
def test_bark_one_word():
    assert bark("hello") == "bark"


def test_bark_two_words():
    assert bark("hello world") == "bark bark"


def test_bark_four_words():
    assert bark("I love my dog") == "bark bark bark bark"


def test_bark_returns_string():
    assert isinstance(bark("hello"), str)


def test_bark_empty_string():
    with pytest.raises(ValueError):
        bark("")


def test_bark_whitespace_only():
    with pytest.raises(ValueError):
        bark("   ")


def test_bark_not_a_string():
    with pytest.raises(TypeError):
        bark(123)


def test_bark_none():
    with pytest.raises(TypeError):
        bark(None)


# ---- WAG TESTS (YOUR PART) ----
def test_wag_returns_string():
    result = wag("hello")
    assert isinstance(result, str)


def test_wag_contains_message():
    result = wag("hello")
    assert "hello" in result


def test_wag_ascii_present():
    result = wag("hi")
    assert "~wag~" in result


def test_wag_empty_string():
    with pytest.raises(ValueError):
        wag("")


def test_wag_not_string():
    with pytest.raises(TypeError):
        wag(123)