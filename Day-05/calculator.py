import sys
import os

def add(a, b):
    return a + b  

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

a = int(sys.argv[1])
b = int(sys.argv[3])
operator = sys.argv[2]

if operator == '+':
    result = add(a, b)
    print(result)
elif operator == '-':
    result = subtract(a, b)
elif operator == '*':
    result = multiply(a, b)


password = os.getenv("PASSWORD")

print(password)