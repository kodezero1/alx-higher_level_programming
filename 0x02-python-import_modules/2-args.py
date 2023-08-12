#!/usr/bin/python3

"""
This script prints the number of arguments provided on the command line and lists them.
"""

import sys

def main():
    # Calculate the number of command-line arguments
    count = len(sys.argv) - 1

    # Handle different cases based on the number of arguments
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # List and number the provided arguments
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

if __name__ == "__main__":
    # Execute the main function
    main()
