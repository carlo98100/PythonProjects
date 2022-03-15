

import random

global guess
global rightNumber
global firstTime
global stop
global keepGoing


rightNumber = random.randint(1, 100)
firstTime = True
keepGoing = True


print("Welcome to Guess the number")
print(rightNumber)



# def CheckIfRightNumber():
#     if(guess == rightNumber) :
#         print("Rätt")
#         keepGoing = False
#     else :
#         print("Inte rätt")
#         guess = int(input("Wrong number, try again: "))


while(keepGoing) :

    if(firstTime == True) :
        guess = int(input("Guess a number: "))
        firstTime = False


    if(guess == rightNumber) :
        print("Rätt")
        keepGoing = False
    else :
        print("Inte rätt")
        guess = int(input("Wrong number, try again: "))
