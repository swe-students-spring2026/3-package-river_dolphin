from .core import speak, bark, wag
import argparse
# use arg parse to create a command line interface for the pydog package.
def main():
    parser = argparse.ArgumentParser(description="pydog - a dog in your terminal")
    parser.add_argument("--bark", type=int, help="enter a number to specify the number of barks")
    parser.add_argument("--wag", type=str, help="enter a message for the dog to wag")

    parser.add_argument("--speak-message", type=str, help="message for speak")
    parser.add_argument("--speak-mood", type=str, help="mood for speak (happy, sleepy, angry)")

    
    args = parser.parse_args()
    
    if args.bark is not None:
        print(bark(args.bark))
    elif args.wag is not None:
        print(wag(args.wag))
    elif args.speak_message is not None and args.speak_mood is not None:
        print(speak(args.speak_message, args.speak_mood))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()