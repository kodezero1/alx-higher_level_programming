#!/usr/bin/python3

"""
This program imports functions from the calculator_1.py file, performs mathematical operations,
and prints the result using a and b as arguments.
"""

from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5
    
    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)
    
    print("Result of adding {} and {}: {}".format(a, b, addition_result))
    print("Result of subtracting {} from {}: {}".format(b, a, subtraction_result))
    print("Result of multiplying {} and {}: {}".format(a, b, multiplication_result))
    print("Result of dividing {} by {}: {}".format(a, b, division_result))

if __name__ == "__main__":
    main()
