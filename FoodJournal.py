NewEntry = 1
LookUp = 2
Quit = 3


def menu():
    # C9-1 Using a dictionary to store the Taste Journal
    TasteJournal = {}

    choice = 0
    while choice != Quit:
        choice = int(input('Welcome to the Taste Journal! Enter 1 to add a new entry, '
                           'or 2 to look up an existing entry. Enter 3 to quit.  '))
        if choice == 1:
            newfood = input('What food do you want to add?   ')
            foodtaste = input('How did it taste?   ')
            TasteJournal[newfood] = foodtaste
        if choice == 2:
            food = input('What is the food?   ')
            print(f'{food}:', TasteJournal.get(food, 'Not found'))


menu()