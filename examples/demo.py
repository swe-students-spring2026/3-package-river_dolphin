from pydog import speak, bark, wag, pose

if __name__ == "__main__":
    print("=== SPEAK ===")
    print(speak("hello!", "happy"))
    print()
    print(speak("I'm tired...", "sleepy"))

    print("\n=== BARK ===")
    print(bark(3))
    print()
    print(bark(5))

    print("\n=== WAG ===")
    print(wag("good dog"))
    print()
    print(wag("fetch!"))

    print(pose("sit", "sleepy"))
    print()
    print(pose("stand", "happy"))
    print()
    print(pose("stare", "angry"))
    print()
    print(pose("stare", "sleepy"))