import datetime
import random
import re
import keyboard


#Custom method that validates if the Birth date is in current format [yyyymmdd]
def ValidateDateFormat(date):

   try:    
      # Validates the date
      
      datetime.datetime.strptime(date, "%Y%m%d")
      return True

   # If the date validation goes wrong
   except ValueError:
      return False

#Custom method that calculates the age from a birthdate.
def CalculateAge(birthDate):
    today = datetime.datetime.today()
    birthDate = datetime.datetime.strptime(birthDate, "%Y%m%d")

    return today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

#Makes the diff change in the list and removes the objects that differs more than accepted.
def RemoveDiffValues(list, rightNumber, maxMinValue):
   shorter_List = []
   for x in list:
      if x <= (rightNumber + maxMinValue) and x >= (rightNumber - maxMinValue):
         shorter_List.append(x)
   
   return shorter_List

#Removes the guessed number from the list.
def RemoveGuessedNumber(guessedNumber, list):
   for x in list:
      if x == guessedNumber:
         
         list.remove(x)
   return list

#Validates the Full name so it has two strings with only one space between
def CorrectFullNameFormat(input):
   if re.match(r"^([A-Öa-ö]*\s[A-Öa-ö]*)$", input, re.IGNORECASE):
      return True
   else:
      return False



print("Welcome to \"Guess the number\"!")
player_Name = input("Please type your full name [Firstname] [Lastname]:\nYour answer: ")

#If the fullname is not in the correct format then let the user type it in again
while not CorrectFullNameFormat(player_Name):
   player_Name = input("Oops, seems like the format on your name wasn't correct, pls try again with following format [Firstname] [Lastname]:\nYour answer: ")

#Lets the player type in the birthdate
player_BirthDate = input("\nGreat, now we need to confirm that you are over 18 years old, So please insert your birth date in following format [yyyy:mm:dd]:\nYour answer: ")

#Validates that the typed birthdate is in the right format and if not, then it lets the user typee it again.
while not ValidateDateFormat(player_BirthDate)  or (CalculateAge(player_BirthDate) < 18) :

   if not ValidateDateFormat(player_BirthDate): 
      player_BirthDate = input("The format of your birth date was not right. Please try again:\nYour answer: ")
   
   elif (CalculateAge(player_BirthDate) < 18):
      player_BirthDate = input("Sorry you where to young for this game, Please try again:\nYour answer: ")




#Here is the start of the actual game.
gameIsOn = True
while gameIsOn:
   #generates a list with random numbers between 0 - 100
   lucky_List =[]

   for x in range(10):
      lucky_List.append(random.randint(0, 100))

   #generates a random "Lucky number" that are random between 0 - 100 and adds it to the list.
   lucky_Number = random.randint(0, 100)
   lucky_List.append(lucky_Number)

   #Creating a counter so we can check how many times that the user have tried to guess.
   tries_Count = 1

   wrongNumber = True

   while wrongNumber:
      #Askes the player to type in a number from the list
      player_Input = input(f"\nPick a number of following:\n{lucky_List}\n\nYour answer: ")

      #If the number that the user types in isn't the right number, then it starts to remove som numbers from the list
      #That differs more than 10 from the lucky number
      if(lucky_Number != int(player_Input)):   

         #Here i use the function created above.  
         shorter_Lucky_List = RemoveDiffValues(lucky_List, lucky_Number, 10)
         
         while wrongNumber:
            tries_Count += 1
            player_Input = input(f"this is try#{tries_Count} and new list is:{shorter_Lucky_List}, choose the lucky number?\nYour answer: ")

            #Here is the validate again if the user have typed in the right number
            if (lucky_Number != int(player_Input)):
               #If its the wrong number, then i use one of the functions above to remove it from the list.
               shorter_Lucky_List = RemoveGuessedNumber(int(player_Input), shorter_Lucky_List)
            else:
               #If the user guesses the number right then it shows that the user won.
               print(f"\nGongrats, game is over! And you got lucky number from try #{tries_Count} :)")
               wrongNumber = False
               # gameIsOn = False

      else:
          #If the user guesses the number right then it shows that the user won.
         print(f"\nGongrats, game is over! And you got lucky number from try #{tries_Count} :)")
         wrongNumber = False
         # gameIsOn = False

   print("Now the game is over! Do you want to play again? [Y]/[N]?")
   while gameIsOn:
    #Here i check if the user presses the Y button or the N button.
    #If they press Y then the game restarts.
    if keyboard.is_pressed('y'):
        gameIsOn = True
        break
    #Otherwise it ends the game.
    elif keyboard.is_pressed('n'):
        gameIsOn = False
        break