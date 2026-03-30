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

# This function generates a string representation of a dog barking a specified number of times.
def bark(num_barks: int) -> str:
    if not isinstance(num_barks, int) or isinstance(num_barks, bool):
        raise TypeError(f"num_barks must be an int, got {type(num_barks).__name__}")
    if num_barks <= 0:
        raise ValueError("num_barks must be a positive number")

    barks = " ".join(["bark"] * num_barks)
    border = "-" * (len(barks) + 2)
    bubble = f" {border}\n< {barks} >\n {border}\n   \\\n    \\"
    return f"{bubble}\n{DOGS['dog1']}"


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