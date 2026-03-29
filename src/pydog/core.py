def speak(message: str, mood: str) -> str:
    if not isinstance(message, str) or not message.strip():
        raise ValueError("message must be a non-empty string")

    if not isinstance(mood, str):
        raise ValueError("mood must be a string")

    mood = mood.strip().lower()

    VALID_MOODS = {"happy", "sleepy", "angry"}

    if mood not in VALID_MOODS:
        raise ValueError(f"Invalid mood: {mood}")

    speech = f"""  ___________
< {message.strip()} >
  -----------"""

    if mood == "happy":
        dog = r"""
  ___    ___
 / / \__/ \ \
 \/| /\/\ |\/
  _||^  ^||_
 /. .\__/. .\
/ . .(__) . .\
\ .  \__/  . /
 \__/\__/\__/
"""
    elif mood == "sleepy":
        dog = r"""
  ___    ___.  zzzz
 / / \__/ \ \ /
 \/| /\/\ |\/
  _||-  -||_
 /. .\__/. .\
/ . .(__) . .\
\ . ----- . /
 \__/\__/\__/
"""
    else:
        dog = r"""
           __      _
        \.'---.//|
         |\./|  \/
        _|.|.|_  \
       /(  ) ' '  \
      |  \/   . |  \
WOOF!  \_/\__/| |
        V  /V / |
          /__/ /
          \___/\
"""

    return speech + dog


DOGS = {
    "dog1": r"""
        / \__
       (    @\___
       /         O
      /   (_____/
     /_____/   U
"""
}


def bark(message: str) -> str:
    if not isinstance(message, str):
        raise TypeError(f"message must be a string, got {type(message).__name__}")
    if not message.strip():
        raise ValueError("message cannot be empty or whitespace")

    word_count = len(message.split())
    barks = " ".join(["bark"] * word_count)
    return barks


def wag(message: str) -> str:
    if not isinstance(message, str):
        raise TypeError(f"message must be a string, got {type(message).__name__}")
    if not message.strip():
        raise ValueError("message cannot be empty or whitespace")

    dog = r"""
      / \__
     (    @\___
     /         O
    /   (_____/
   /_____/   U   ~wag~
    """

    speech = f"""  ___________
< {message.strip()} >
  -----------"""

    return speech + dog