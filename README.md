# Python Package Exercise
![CI](https://github.com/swe-students-spring2026/3-package-river_dolphin/actions/workflows/build.yaml/badge.svg)

A Python package exercise `pyfundog` lets you generate ASCII dogs that can **speak, bark, wag, and pose**.

See [instructions](./instructions.md) for details.

---

## Team members:
[Tsengelmurun Enkh-Onon](https://github.com/murnbn)
[Milan Engineer](https://github.com/MilanEngineer)
[Sara Dou](https://github.com/SaraD-666)
[Jack Escowitz](https://github.com/JackREscowitz)


## Features
### speak(message, mood)

Returns a dog ASCII with a message and mood (happy, sleepy, angry)

Example:
```
from pyfundog import speak

print(speak("hello!", "happy"))

```

### bark(num_barks)

Returns a dog ASCII with a speech bubble containing "bark" repeated `num_barks` times

Example:
```
from pyfundog import bark

print(bark(3))

```

### wag(message)

Returns a wagging dog ASCII that echoes the message

Example:
```
from pyfundog import wag

print(wag("Good dog!"))

```

### pose(trick, mood)

Returns a dog ASCII performing a specific trick with a given mood.

Valid tricks: sit, stand, stare

Valid moods: happy, sleepy, angry

Raises:

- ValueError if trick or mood is invalid

Example:
```
from pyfundog import pose

print(pose("sit", "happy"))
print(pose("stand", "sleepy"))
print(pose("stare", "angry"))

```

## install from PyPI:

https://pypi.org/project/pyfundog/0.1.0/

```
pip install pyfundog

```

## Usage (CLI)
```
python -m pyfundog --bark 3
python -m pyfundog --wag "hello"
python -m pyfundog --speak-message "hi" --speak-mood happy

```

## Example Program

Run the demo:
```
pipenv run python examples/demo.py
```

## Developer Setup:

```
#Python 3.9, 3.10, 3.11

# Clone repo:
git clone https://github.com/swe-students-spring2026/3-package-river_dolphin.git
cd 3-package-river_dolphin

# Install pipenv: 
pip install pipenv

# Install dependencies:
pipenv install --dev
pipenv install -e .

# Run tests:
pipenv run pytest

# Build package:
pipenv run python -m build
```

## Contributing:

```
# Python 3.9, 3.10, 3.11

# Create a feature branch:
git checkout -b feature/your-feature

# Make changes and test: 
pipenv run pytest

# Commit and push:
git add .
git commit -m "Add feature"
git push origin feature/your-feature

# Open a PR on GitHub
```

## License:
Licensed under the MIT License. See [License](./LICENSE).

## Course Exercise:
This repository is part of the package engineering exercise documented in [instructions](./instructions.md).