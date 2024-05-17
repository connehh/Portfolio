# Badges
# C2-1 (User input)
# C2-2 (Print to Console)
# C2-4 (Comments)
# C3-1 (Else/If)
# C3-2 (Boolean)
# C3-3 (Comparisons)

FirstPassword = "function"
SecondPassword = "block"
print("Door: Please provide a password")
FirstGuess = input()
# C2-1 and C2-2 This is a message printed to console, and a user input shown above
# This starts the flow of questions // C2-4 This is a comment to show what I'm doing for this portion of the code
if FirstGuess == FirstPassword:
    # C3-3 Using comparisons to ensure it equals the correct password
    # C3-1 Using the if statement, I was able to ensure it discerns between two passwords
    print("Okay what's the other password?")
elif FirstGuess == SecondPassword:
    print("Okay what's the other password?")
else:
    print("Wrong")
#  C3-2 Used boolean values to the process
SecondGuess = input()
if SecondGuess == FirstGuess:
    SecondGuess = False
elif SecondGuess == FirstPassword or SecondGuess == SecondPassword:
    SecondGuess = True

if SecondGuess == True:
    print("Welcome to the Guild of Calamitous Intent")
else:
    print("Wrong")