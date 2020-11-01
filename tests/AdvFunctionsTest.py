from src.AdvFunctions import int_division, factorial, quadratic_eq
from tests.TestCore import unit_test


def int_division_test():
    unit_test([3, 1], int_division, 10, 3)
    unit_test([-4, -2], int_division, 10, -3)
    unit_test([-4, 2], int_division, -10, 3)
    unit_test([3, -1], int_division, -10, -3)
    unit_test(ZeroDivisionError, int_division, 1, 0)


def factorial_test():
    unit_test(1, factorial, 0)
    unit_test(1, factorial, 1)
    unit_test(5, factorial, 120)


def quadratic_eq_test():
    unit_test([-1], quadratic_eq, 1, 2, 1)
    unit_test("This quadratic equation does not have real root.", quadratic_eq, 1, 2, 6)
    unit_test([-2, 0], quadratic_eq, 1, 2, 0)


if __name__ == "__main__":
    int_division_test()
    factorial_test()
    quadratic_eq_test()
