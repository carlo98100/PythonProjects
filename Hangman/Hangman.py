import random

global RandomWords
global completeWord
global userGuess
global keepGoing
global firstTime
global charExist
global tries


RandomWords = []


##Reads a file that has many different words.
with open('Hangman\Hangman-Words.txt','r') as file:
    for line in file:

      
        for word in line.split():
       
            RandomWords.append(word)



# Picks a random word from the files content.
completeWord = RandomWords[random.randint(0, len(RandomWords))].lower()
WordBuild = ""
firstTime = True
keepGoing = True
charExist = False
tries = int(0)

#Generates question marks for the word.
for char in completeWord :
    WordBuild += "?"


#A method for the draws in the game.
def DrawHangMan(tries):
    match tries:
        case 1:
            print("________\n")
        case 2:
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________\n")
        case 3:
            print("________")
            print("|/")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________\n")
        case 4:
            print("________")
            print("|/      |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________\n")
        case 5:
            print("________")
            print("|/      |")
            print("|       0")
            print("|      / \\")
            print("|       |")
            print("|      / \\")
            print("|")
            print("|________\n")
            

#This method checks the char that the user was guessing against the word and sees if it exists inside the word or not.
def checkIfCharExist(word, userGuess):
    global tries
    global WordBuild
    isCharFound = False
    for index, char in enumerate(word, start=0):
        if char == userGuess:
            isCharFound = True
            break

#If the char do exist, then it loops through the whole word and replaces the question marks with the char.
    if(isCharFound == True):
        for index, char in enumerate(word, start=0):
            if char == userGuess:
                WordBuild = WordBuild[:index] + char + WordBuild[index + 1:]
        
        
        print(WordBuild)
        return True
#If the char does not exist. Then it draws out a little bit of the whole drawing and increse the tries.
    else:
            tries += 1
            DrawHangMan(tries)
            return False
    
    
    

print(completeWord)
print("Welcome to the hangman")
print(WordBuild)

while (completeWord != WordBuild and tries < 5):
    if(firstTime == True and charExist == False):
        userGuess = input("Guess a character: ").lower()
        charExist = checkIfCharExist(completeWord, userGuess)
        firstTime = False
    elif(firstTime == False and charExist == True):
        userGuess = input("Good job you find one of the characters in the word! Try one more: ").lower()
        charExist = checkIfCharExist(completeWord, userGuess)
    else:
        userGuess = input("Sorry, that character dosen't exist in the current word, try again: ").lower()
        charExist = checkIfCharExist(completeWord, userGuess)

if(completeWord == WordBuild) :
    print("Good job you won!")
