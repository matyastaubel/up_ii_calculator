from src.FunctionManager import FunctionManager
from src.BasicFunctions import add, subtract, multiply, divide


# Runs the calculator.
def calculate():
    func_manager = FunctionManager()

    # Allows user to choose operation.
    func_manager.show_functions()
    user_choice = int_input(len(func_manager.functions))

    # Calculates number of needed arguments.
    num_of_args = func_manager.calc_num_of_args(user_choice)

    # Asks user to enter number of inputs needed for chosen operation.
    nums = get_function_args(num_of_args)

    # This actually calculates result and prints it.
    print('''The result is {}'''.format(
        func_manager.use_function(user_choice, *nums)
    ))

    # Asks users if they want to do more calculations.
    again()


#
def get_function_args(num_of_args):
    print("The function is accepting {} numbers".format(num_of_args if num_of_args != 0 else "infinite"))

    # Asks user to enter number of inputs needed for chosen operation.
    nums = []
    for i in range(num_of_args):
        nums.append(float_input())

    # In case that we have function with not defined number of arguments.
    if len(nums) == 0:
        print("Stop giving numbers by entering \"stop\"")
        user_input = input("Enter a number:")
        while user_input != "stop":
            nums.append(float_input())
            user_input = input("Enter a number: ")

    return nums


# Catches exceptions if user is dumb enough to enter nonsense
def int_input(num_of_funcs):
    while True:
        try:
            user_input = float(input("Enter a number: "))
        except ValueError:
            print("Wrong input, try it again.")
        else:
            if user_input in range(num_of_funcs):
                return user_input
            else:
                print("Wrong input, try it again.")
                continue


# Catches exceptions if user is dumb enough to enter nonsense
def float_input():
    while True:
        try:
            user_input = float(input("Enter a number: "))
        except ValueError:
            print("Wrong input, try it again.")
        else:
            return user_input


# Asks users if they want to use the calculator again
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types something else, run the function again
    else:
        print('Wrong input. Try it one more time.\n')
        again()



if __name__ == "__main__":
    calculate()
