import math

# define functions : addition, subtraction, multiplication, division

user_choice = 0


def add():
    get_user_input()
    addition_result = first_number + second_number
    print(addition_result)
    return addition_result


def subtract():
    get_user_input()
    subtraction_result = first_number - second_number
    print(subtraction_result)
    return subtraction_result


def multiply():
    get_user_input()
    multiplication_result = first_number * second_number
    print(multiplication_result)
    return multiplication_result


def division():
    get_user_input()
    division_result = first_number / second_number
    print(division_result)
    return division_result


# print options for the user
def user_options():
    user_choice = int(
        input(
            "For Addition (+) please enter 1\n for subtraction (-) please enter 2 \n for multiplication (x) please enter 3\n for division (/) please enter 4\n "
        )
    )

    if user_choice == 1:
        add()
    elif user_choice == 2:
        subtract()
    elif user_choice == 3:
        multiply()
    elif user_choice == 4:
        division()
    else:
        print("Wrong entry, please choose from 1 to 4 \n ")
        user_options()


# get user input
def get_user_input():
    global first_number
    global second_number
    first_number = int(input("Please enter the first number: "))
    second_number = int(input("Please enter the first number: "))


user_options()
