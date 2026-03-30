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
def test_bark_one():
    assert "bark" in bark(1)

def test_bark_three():
    result = bark(3)
    assert result.count("bark") == 3

def test_bark_returns_string():
    assert isinstance(bark(1), str)

def test_bark_has_bubble():
    result = bark(2)
    assert "<" in result and ">" in result

def test_bark_has_dog():
    result = bark(1)
    assert "___" in result  # part of the dog art

def test_bark_zero():
    with pytest.raises(ValueError):
        bark(0)

def test_bark_negative():
    with pytest.raises(ValueError):
        bark(-1)

def test_bark_not_an_int():
    with pytest.raises(TypeError):
        bark("hello")

def test_bark_none():
    with pytest.raises(TypeError):
        bark(None)

def test_bark_bool():
    with pytest.raises(TypeError):
        bark(True)


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