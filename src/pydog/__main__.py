from .core import wag, bark
import argparse
# use arg parse to create a command line interface for the pydog package
def main():
    parser = argparse.ArgumentParser(description="pydog - a dog in your terminal")
    parser.add_argument("--bark", type=int, help="enter a number to specify the number of barks")
    parser.add_argument("--wag", type=str, help="enter a message for the dog to wag")

    
    args = parser.parse_args()
    
    if args.bark:
        print(bark(args.bark))
    elif args.wag:
        print(wag(args.wag))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()