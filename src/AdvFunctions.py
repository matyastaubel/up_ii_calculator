# More complicated functions to implement

# Returns both result of integer division and modulo
def int_division(num1, num2):
    div=num1 // num2
    mod= num1 % num2
    return [div, mod]


# Returns factorial of given number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to complete the factorial : "))
print(factorial(n))


# Returns all solutions of given quadratic equation
def quadratic_eq(qdr_coef, lin_coef, const):
    return NotImplemented


