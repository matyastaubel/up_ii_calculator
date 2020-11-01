from src.StatisticalFuncions import mean, mode, first_quartile
from tests.TestCore import unit_test


def mean_test():
    unit_test(-3, mean, -10, 0, 1)
    unit_test(35, mean, 2, 3, 100)


def mode_test():
    unit_test(-10, mode, -10)
    unit_test(7.5, mode, 0, 15, 10, 5)
    unit_test(3, mode, 2, 3, 100)


def first_quartile_test():
    unit_test(-10, first_quartile, -10)
    unit_test(0.25, first_quartile, 0, 5, 10, 15, 0, 4, 1)
    unit_test(2.5, first_quartile, 2, 3, 4, 100)


if __name__ == "__main__":
    mean_test()
    mode_test()
    first_quartile_test()
