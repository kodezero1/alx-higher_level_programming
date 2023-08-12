#!/usr/bin/python3

"""
Print all names defined by the hidden_4 module, excluding hidden names.
"""

import hidden_4

def main():
    # Get a list of names defined in the hidden_4 module
    names = dir(hidden_4)
    
    # Print non-hidden names
    for name in names:
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    # Execute the main function
    main()
