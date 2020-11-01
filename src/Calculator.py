from src.ChooseFunction import show_functions, use_function, calc_num_of_args


# Runs the calculator.
def calculate():

    # Allows user to choose operation.
    show_functions()
    user_choice = int(input("Enter number of selected operation: "))

    # Calculates number of needed arguments.
    num_of_args = calc_num_of_args(user_choice)
    print("You have to enter {} numbers".format(num_of_args))

    # Asks user to enter number of inputs needed for chosen operation.
    nums = []
    for i in range(num_of_args):
        nums.append(float(input("Enter a number: ")))

    # This actually calculates result and prints it.
    print('''The result is {}'''.format(
        use_function(user_choice, *nums)
    ))

    # Asks users if they want to do more calculations.
    again()


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
