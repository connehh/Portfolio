import random
again = 'y'

print("Let's play a guessing game!")
print("Pick a number between 1-10 and I'll tell you if you're right!")
print("Let's start...")
print(".....")
print(".....")

while again == 'Y'.lower():

    randomnumber = random.randint(1, 10)

    print("Okay, I'm ready!")
    playersguess = input("Let's see if you can guess the number: ")

    if playersguess == randomnumber:
        print('Great guess!')
        print("Now let's take it further..")
        playersguess2 = input("Guess a number between 1 and 50: ")
        randomnumber2 = random.randint(1, 50)
        if playersguess2 == randomnumber2:
            print("WOW! Amazing work")
        else:
            print(f"That's too bad, the number was actually {randomnumber2}")
            again = input("Wanna try again? Y/N: ")

    else:
        print('Nice Try!')
        print(f"The number was actually {randomnumber}")
        again = input('Wanna try again? Y/N: ')