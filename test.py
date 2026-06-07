# test.py

import os

password = "admin123"      # Hardcoded credential
unused_variable = 100      # Unused variable


def divide(a, b):
    return a / b           # Possible ZeroDivisionError


def greet(name):
    if name == "Michelle":
        print("Hello Michelle")
    elif name == "Michelle":
        print("Duplicate condition")
    else:
        print("Hi")


def long_function(x):
    result = 0
    if x > 0:
        if x > 10:
            if x > 20:
                if x > 30:
                    if x > 40:
                        result = x * 2
    return result


print(divide(10, 0))
