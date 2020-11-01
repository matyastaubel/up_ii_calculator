from src.BasicFunctions import add, subtract, multiply, divide


def use_function(choice,*args):
    return functions[choice][0](*args)


def calc_num_of_args(choice):
    return functions[choice][1]


functions = {
    0: (add, 2),
    1: (subtract, 2),
    2: (multiply, 2),
    3: (divide, 2)
}


# Shows users which function of calculator they can choose
def show_functions():

    print("Please select operation by choosing its number -\n"
          "0 - Add\n"
          "1 - Subtract\n"
          "2 - Multiply\n"
          "3 - Divide\n")