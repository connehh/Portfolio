

print("How many books have you purchased today?")
Books = int(input())
if Books == 0:
    print("You have gained 0 points")
elif Books == 1:
    print("You have gained 5 points")
elif Books == 2:
    print("You have gained 15 points")
elif Books == 3:
    print("You have gained 30 points")
else:
    print("You have gained 60 points")
