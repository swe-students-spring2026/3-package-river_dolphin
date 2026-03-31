from .core import wag, bark, pose
import argparse
# use arg parse to create a command line interface for the pydog package.
def main():
    parser = argparse.ArgumentParser(description="pydog - a dog in your terminal")
    parser.add_argument("--bark", type=int, help="enter a number to specify the number of barks")
    parser.add_argument("--wag", type=str, help="enter a message for the dog to wag")
    parser.add_argument("--pose", nargs=2, metavar=("TRICK", "MOOD"))

    
    args = parser.parse_args()
    
    if args.bark:
        print(bark(args.bark))
    elif args.wag:
        print(wag(args.wag))
    elif args.pose:
        trick, mood = args.pose
        print(pose(trick, mood))
    else:
        print(bark(2))
        print(wag("good dog"))
        print(pose("sit", "happy"))
        # parser.print_help()
        # I think it will be cuter to show the demos for default

if __name__ == "__main__":
    main()