from src.BasicFunctions import add, subtract, multiply, divide
from tests.TestCore import basic_test


# tests if add() works for zero, positive numbers and negative numbers
def add_test():
    basic_test(10.6, 5.4, add, 16)
    basic_test(-10, 5, add, -5)
    basic_test(0, 5, add, 5)


# tests if subtract() works for zero, positive numbers and negative numbers
def subtract_test():
    basic_test(10.4, 5.4, subtract, 5)
    basic_test(-10, 5, subtract, -15)
    basic_test(0, 5, subtract, -5)


# tests if multiply() works for zero, positive numbers and negative numbers
def multiply_test():
    basic_test(0, 5, multiply, 0)
    basic_test(5, 5, multiply, 25)
    basic_test(-5, 5, multiply, -25)
    basic_test(-5, -5, multiply, 25)


# tests if multiply() works for zero, positive numbers and negative numbers
def divide_test():
    basic_test(0, 5, divide, 0)
    basic_test(10, 5, multiply, 2)
    basic_test(-10, 5, multiply, -2)
    basic_test(-5, -10, multiply, 0.5)
    basic_test(5, 0, multiply, ZeroDivisionError)


if __name__ == "__main__":
    add_test()
    subtract_test()
    multiply_test()
    divide_test()
