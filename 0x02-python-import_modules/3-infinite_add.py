#!/usr/bin/python3

"""
Print the sum of all command-line arguments.
"""

import sys

def main():
    # Initialize the total sum
    total = 0

    # Iterate through command-line arguments and add to the total
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])

    # Print the total sum
    print("Sum of arguments: {}".format(total))

if __name__ == "__main__":
    # Execute the main function
    main()
