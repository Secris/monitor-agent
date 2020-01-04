import sys

def main():
    if sys.platform == "linux":
        print("Hello, Linux!")
    else:
        print("OS not supported")


if __name__ == "__main__":
    main()
