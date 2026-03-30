from pydog import speak, bark, wag, pose

if __name__ == "__main__":
    print("=== SPEAK ===")
    print(speak("hello!", "happy"))

    print("\n=== BARK ===")
    print(bark("hello world"))

    print("\n=== WAG ===")
    print(wag("good dog"))

    print(pose("sit", "sleepy"))
    print()
    print(pose("stand", "happy"))
    print()
    print(pose("stare", "angry"))