import random
personal = ['Normal', 'Lazy', 'Sisterly', 'Snooty', 'Cranky', 'Jock', 'Peppy', 'Smug']
hobby = ['Education', 'Fashion', 'Fitness', 'Music', 'Nature', 'Playing']
name = input('What is the name of your Villager?')

# C7-1 Using random integers to create unique villagers
# C6-1 Try/Except in the event it would cause it to crash
try:
    rpersonal = random.randint(0, 7)
    rhobby = random.randint(0, 5)
except IndexError as a:
    print(a)

print(f'{name} is {personal[rpersonal]} and into {hobby[rhobby]}')