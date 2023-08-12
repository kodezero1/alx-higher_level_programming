#!/usr/bin/python3

"""
This module defines basic mathematical operations.
"""

def add(a, b):
    """Addition"""
    return a + b

def sub(a, b):
    """Subtraction"""
    return a - b

def mul(a, b):
    """Multiplication"""
    return a * b

def div(a, b):
    """Division"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
