#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    return "Sunny"
greet_with_default("Sunny")
greet_with_default()



def add(num1, num2):
    return num1 + num2

result = add(1, 2)
print(result)  # Output: 3


def halve(number):
    if not isinstance(number, (int, float)):
        return None  # Return None if the input is not a number
    result = number / 2
    print(result)  # Print the result
    return result  # Return the result as well

# Example call:
halve(10)  # Output: 5.0
