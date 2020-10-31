

# Method for testing methods with two numbers on input.
def basic_test(num1, num2, function, expected):
    test_name = "{} {}, {}".format(function, num1, num2)
    result = function(num1, num2)
    assert_result(result, expected, test_name)


# Compare expected and actual result of tested method. Has to be imported for each layer of unit tests.
def assert_result(result, expected, test_name):
    if result == expected:
        print("{} - OK".format(test_name))
    else:
        print("{} - FAILED. Expected {} but was {}.".format(test_name, expected, result))