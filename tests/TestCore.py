

# Method for testing methods with two numbers on input.
def unit_test(expected, function, *args):
    test_name = "{} {}".format(function, *args)
    result = function(*args)
    assert_result(result, expected, test_name)


# Compare expected and actual result of tested method. Has to be imported for each layer of unit tests.
def assert_result(result, expected, test_name):
    if result == expected:
        print("{} - OK".format(test_name))
    else:
        print("{} - FAILED. Expected {} but was {}.".format(test_name, expected, result))