

global completeWord
global userGuessing
global keepGoing
global firstTime

completeWord = "apple"
userGuessing = ""
firstTime = True
keepGoing = True

for char in completeWord:
    userGuessing += "?"




print("Welcome to the hangman")

while(keepGoing) :

    if(firstTime == True) :

        userGuessing = input("Guess a number: ")
        firstTime = False
        
