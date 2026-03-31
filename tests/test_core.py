import pytest
from pydog.core import speak, bark, wag, fetch, pose


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


def test_pose_sit_happy():
    result = pose("sit", "happy")
    assert "sit" in result.lower()
    assert "happy" in result.lower() or "happily" in result.lower()
    assert isinstance(result, str)

def test_pose_stand_sleepy():
    result = pose("stand", "sleepy")
    assert "stand" in result.lower()
    assert isinstance(result, str)
    assert len(result) > 0

def test_pose_stare_angry():
    result = pose("stare", "angry")
    assert "stare" in result.lower()
    assert "angry" in result.lower() or len(result) > 0
    assert isinstance(result, str)

def test_pose_invalid_trick():
    with pytest.raises(ValueError):
        pose("jump", "happy")

def test_pose_invalid_mood():
    with pytest.raises(ValueError):
        pose("sit", "excited")

def test_pose_invalid_type():
    with pytest.raises(ValueError):
        pose("", "happy")


# ---- FETCH TESTS ----
def test_fetch_returns_string():
    assert isinstance(fetch("ball"), str)


def test_fetch_contains_item():
    result = fetch("stick")
    assert "stick" in result


def test_fetch_different_items():
    result1 = fetch("ball")
    result2 = fetch("frisbee")
    assert result1 != result2


def test_fetch_strips_whitespace():
    result = fetch("  bone  ")
    assert "bone" in result


def test_fetch_has_dog():
    assert "___" in fetch("ball")


def test_fetch_empty_string():
    with pytest.raises(ValueError):
        fetch("")


def test_fetch_not_string():
    with pytest.raises(TypeError):
        fetch(42)