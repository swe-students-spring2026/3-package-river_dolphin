# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Features

### speak(message, mood)

Returns a dog ASCII with a message and mood (happy, sleepy, angry)

### bark(num_barks)

Returns "bark" repeated for each word in the input

### wag(message)

Returns a wagging dog ASCII that echoes the message

### pose(trick, mood)

Returns a dog ASCII performing a specific trick with a given mood.

Valid tricks: sit, stand, stare

Valid moods: happy, sleepy, angry

Raises:

- ValueError if trick or mood is invalid

Example:
```
from pydog import pose

print(pose("sit", "happy"))
print(pose("stand", "sleepy"))
print(pose("stare", "angry"))

```

## Run Instructions (temp-- update later)

```
pip install pipenv

# Install dependencies:

pipenv install

# Activate the virtual environment:

pipenv shell

# run the package

python -m pydog


```

## Example Program

Run the demo:

(update it to run demo.py) 