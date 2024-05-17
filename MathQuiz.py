import random


# C5-2 "def main" is my primary function that keeps everything together.
def main():
    # C5-4 "again = 'y'" is a local scope since it exists only within this function.
    # A global scope would be a variable set outside the function.
    again = 'y'

    while again == 'y' or again == 'Y':
        # C5-3 Here is my first implementation of a module, to randomly select between adding or subtracting
        aos = random.randint(1, 2)
        if aos == 1:
            add()
        elif aos == 2:
            subtract()

        again = input('Would you like another math question? (y = yes): ')


def add():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    guess = int(input(f'What is {num1} + {num2}: '))
    total = num1 + num2
    if guess == total:
        # C5-1 Implementing a return function to return the answer back to the user
        return "You are correct!"
    elif guess != total:
        return f"You are incorrect, the answer is {total}"


def subtract():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    guess = int(input(f'What is {num1} - {num2}: '))
    total = num1 - num2
    if guess == total:
        return "You are correct!"
    elif guess != total:
        return f"You are incorrect, the answer is {total}"


main()
