print("While exploring the woods, you come upon a decayed structure of a house..")
print("While approaching, everything seems to become darker and you feel something pulling you towards the house")
print("You find yourself in the house. From the entrance, you see a kitchen, a bathroom, and a door in the back.")
print("-----------")
print("Press 1 to explore the kitchen, 2 to explore the bathroom, 3 to explore the creepy door, and 0 to leave")

total = 0

choice = int(input())
# C4-1 Using a while loop to contain the choices.
while choice != 0:

    if choice == 1:
        print("You walk into the kitchen. Before you're able to focus on anything, the overwhelming smell of rotten")
        print("food fills your senses. the kitchen is dilapidated and mold covers the walls and floor.")
        hours = 1
        total += hours
    elif choice == 2:
        print("As you enter, you wonder why you decided checking the bathroom was a good choice. As the smell of mold")
        print("and rotten whatever-that-is fills your nose, you think you can make out a shadow behind the curtain.")
        print("The more you stare at the shower curtain, the more it becomes larger. You avert your gaze.")
        hours = 1
        total += hours
    elif choice == 3:
        print("You walk towards the creepy door. As you begin to open the door, something pushes the door closed.")
        print("You try again and manage to open it. As you walk through and make out your surroundings, you realize")
        print("it's the hallway you entered through. You turn around and see the creepy door. It's closed.")
        hours = 1
        total += hours

    print("------------")
    print("Press 1 to explore the kitchen, 2 to explore the bathroom, 3 to explore the creepy door, and 0 to leave")
    choice = int(input())

if choice == 0:
    # C2-3 Calculating the total by adding in hours for each iteration
    hours = 1
    total += hours
    print("You leave the house. How long has it been? You check your watch..")
    print("It's been " + str(total) + " hour(s)")
