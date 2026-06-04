from math import *

def math_operations(num):
    if num < 0:
        print("Invalid input")
        return

    print("Square Root:", sqrt(num))
    print("Power:", pow(num, 2))
    print("PI Value:", pi)

math_operations(16)