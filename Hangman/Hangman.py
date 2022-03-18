import random

global RandomWords
global completeWord
global userGuess
global keepGoing
global firstTime
global charExist
global tries


RandomWords = []


with open('Hangman-Words.txt','r') as file:
    for line in file:

      
        for word in line.split():
       
            RandomWords.append(word)




completeWord = RandomWords[random.randint(0, len(RandomWords))].lower()
WordBuild = ""
firstTime = True
keepGoing = True
charExist = False
tries = int(0)


for char in completeWord :
    WordBuild += "?"



def DrawHangMan(tries):
    match tries:
        case 0:
            print("________\n")
        case 1:
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________\n")
        case 2:
            print("________")
            print("|/")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________\n")
        case 3:
            print("________")
            print("|/      |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________\n")
        case 4:
            print("________")
            print("|/      |")
            print("|       0")
            print("|      / \\")
            print("|       |")
            print("|      / \\")
            print("|")
            print("|________\n")
            


print("Welcome to the hangman")
print(WordBuild)

while(completeWord != WordBuild) :
    if(tries < 4) :
        
        if(firstTime == True) :

            userGuess = input("Guess a character: ").lower()
            firstTime = False

        elif(charExist and not firstTime) :
        
            userGuess = input("Good job you find one of the characters in the word! Try one more: ").lower()
            charExist = False

        else :
            DrawHangMan(tries)
            userGuess = input("Sorry, that character dosen't exist in the current word, try again: ").lower()
            tries += 1


        for index, char in enumerate(completeWord, start=0) :

            if(char == userGuess) :
                WordBuild = WordBuild[:index] + char + WordBuild[index + 1:]
                charExist = True

        print(WordBuild)
        
    else:
        DrawHangMan(tries)
        print("Sorry you dont have any more tries. Better luck next time!")
        break

if(completeWord == WordBuild) :
    print("Good job you won!")
