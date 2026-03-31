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

def pose(trick: str, mood: str = "happy") -> str:
    if not isinstance(trick, str) or not trick.strip():
        raise ValueError("trick must be a non-empty string")

    if not isinstance(mood, str):
        raise ValueError("mood must be a string")

    trick = trick.strip().lower()
    mood = mood.strip().lower()

    # might remove roll...cuz it's hard to find roll ASCII art of a dog
    valid_tricks = {"sit", "stand", "stare"}
    valid_moods = {"happy", "sleepy", "angry"}

    if trick not in valid_tricks:
        raise ValueError(f"Invalid trick: {trick}")

    if mood not in valid_moods:
        raise ValueError(f"Invalid mood: {mood}")

    title = f" Dog does {trick}! "

#currently is test, I will replace it with ASCII art of dog doing it
    if trick == "sit":
        if mood == "happy":
            dog = r"""
                     ,--.
                   _/ <`-'
               ,-.' \--\_
              ((`-.__\   )
               \`'    @ (_
               (        (_)
              ,'`-._(`-._/
           ,-'    )&&) ))
        ,-'      /&&&%-'
      ,' __  ,- {&&&&/
     / ,'  \|   |\&&'\
    (       |   |' \  `--.
(%--'\   ,--.\   `-.`-._)))
 `---'`-/__)))`-._)))      HAPPY
            """
        elif mood == "sleepy":
            dog = r"""
                                 _
           / )
        ,-(,' ,---.
       (,-.\,' `  _)-._
          ,' `(_)_)  ,-`--.
         /          (      ) ZZZZZZZ
        /    \        `-.,-'|
       /          --      |/
       |               ,^ /
      /                   |
      |                   /
     /                   /
     |                   |
     |                   |
    /                    \
  ,.|                    |
(`\ |                    |
(\  |   --.      /  \_   |
 (__(   ___)-.   | '' )  /)
     `---...\\\--(__))/-'-' 
            """
        else:
            dog = r"""
~ guard dog ~  9/96

                                        /\ /\
                                       /  \---._
                                      / / `     `\
                                      \ \   `'<@)@)
                                      /`         ~ ~._
                                     /                `()
                                    /    \   (` ,_.:.  /
                                   / ~    `\   (vVvvvvV
                                  /       |`\_ `^^^/
                              ___/________|_  `---'
                             (_____R_E_X____) _
                             _/~          | `(_)
                           _/~             \
                         _/~               |
                       _/~                 |
                     _/~                   |
                   _/~         ~.          |
                 _/~             \        /\
              __/~               /`\     `||
            _/~      ~~-._     /~   \     ||
           /~             ~./~'      \    |)
          /                 ~.        \   )|
         /                    :       |   ||
    jgs  |                    :       |   ||
         |                   .'       |   ||
    __.-`                __.'--.      |   |`---.
 .-~  ___.         __.--~`--.))))     |   `---.)))
`---~~     `-...--.________)))))      \_____)))))
------------------------------------------------
            """

    elif trick == "stand":
        if mood == "happy":
            dog = r"""
                  _ __    ___
     6%'  `--'   `.
     (       o     )
      `--)          \          ,.
       ,'     \      )        (66\
 ,-.   \_      `.__,'\_        )99)
(,-  `.__\,"           `"".__,'  /
(_,-            ,d88b.          /
 (   _      _   888888          (
  `-' `.__,%    `%888' ,         )
            `.       .'         (
              7-.   |            `.
           ,-(   `--",     _,      )
      hjw (,- `._    )`%--"7      (
      `97 (,-     _,"      )       \
          (    _,"        ( (  (    )
           `--'            `"`-"`--"

            """
        elif mood == "sleepy":
            dog = r"""
    __

 o-'. ".    ,.

 `.  |  )   )_)

 __) `-' `-' /

".--         )

 `~--'.__,  (\

   hjw    )  ))
            """
        else:
            dog = r"""
  __      _.

  \.'---.//|

   |\./|  \/

  _|.|.|_  \

 /(  ) ' '  \

|  \/   . |  '.----._____.-----..'}

 \_/\__/| |                     \/

  V  /V / |                      |

    /__/ /                       |

    \___/\ /      \      |       |

          '.\     |______'\     /

           \ |   /       \ \    |

   jrjc     ||  |         ||    |

            ||  |         ||    |

           __|  |       ___.    \

        /// ____)      /// _____/

        \\\(           \\\(
            """

    else:  # stare
        if mood == "happy":
            dog = r"""
  __       __

 /  \_____/  \

 \  / \ / \  /

  \/  / \  \/

 _/_0/   \0_\_

/   \_<o>_/   \

\  \_______/  /

 \   |_|_|   /

  \_________/

     _| |_

    /     \

   /       \

   | |\_/| |

   |_|   |_| 
            """
        elif mood == "sleepy":
            dog = r"""
      ,.

     /  `-._

    /       `.     ___            __

  ,'       _/ ,---'   `-.       ,'  `.

 /   /`---' \/           `--.  /      \

/   |       /             _  `/  -.    `.

\   |              ,.    /O\  \    \     \

 \   `.           /O \  '   `. `. / \    |

  `._  `-.       /   ,   .    ,  `.  \  ,'

     `-.        .   /     `--'     \  \/

        \        `-',d8o8b.        /

         \          dP'88`8b      /

          \  ,'`.     `YP'       |

   -hrr-   \/ .        |       | |

           /  |\       :       |/\

          /   | `.   ,:::     / \ \

         ,\       `-'`""'`.--'  )o )

        (o `.__,               / o/

         \ o   \_           ,-'o /

          \  o  o`-----.__,' o ,'

           `----. o  o  o  o ,'

                 `----------'
            """
        else:
            dog = r"""
   |\

  || \

  | | |

  /.,, /

 (    /

  \  (

   \ \

    \_\__

   .'    '--._    ,__,-.,

  /          _";__( ,__._7

 /           )  \_ Y,=; \d

(         _.'     ~/  6,  '-,

 \___    ;        (   _,-.  Y)

 (C(/\.  )        /I-._\(_'-'

       \_\_,-,_  /,,/  '-7)

          \   |"\_   \   `

           \  _\  \_  \___

            (`  \_  '.<,_)))

  snd        `-\,)))
            """

    border = "-" * len(title)
    return f"{border}\n{title}\n{border}\n{dog}"