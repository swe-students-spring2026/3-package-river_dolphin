import pytest
from pydog.core import speak


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