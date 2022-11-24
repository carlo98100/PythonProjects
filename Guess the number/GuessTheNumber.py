import datetime
import random

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
    


print("Welcome to \"Guess the number\"!")
player_Name = input("Please type your full name [Firstname] [Lastname]:\nYour answer: ")

player_BirthDate = input("\nGreat, now we need to confirm that you are over 18 years old, So please insert your birth date in following format [yyyy:mm:dd]:\nYour answer: ")


while not ValidateDateFormat(player_BirthDate)  or (CalculateAge(player_BirthDate) < 18) :

   if not ValidateDateFormat(player_BirthDate): 
      player_BirthDate = input("The format of your birth date was not right. Please try again:\nYour answer: ")
   
   elif (CalculateAge(player_BirthDate) < 18):
      player_BirthDate = input("Sorry you where to young for this game, Please try again:\nYour answer: ")





gameIsOn = True
while gameIsOn:
   lucky_List =[]

   for x in range(10):
      lucky_List.append(random.randint(0, 100))

   lucky_Number = random.randint(0, 100)
   lucky_List.append(lucky_Number)
   tries_Count = 0
   # print(lucky_Number)

   wrongNumber = True

   while wrongNumber:

      player_Input = input(f"\nPick a number of following:\n{lucky_List}\n\nYour answer: : ")
      tries_Count += 1

      if(lucky_Number == int(player_Input)):
         print(f"\nGongrats, game is over! And you got lucky number from try #{tries_Count} :)")
         wrongNumber = False
         # gameIsOn = False

      else:
         wrongNumber = True
      
      # if(keyboard.read_key() == "y"):
      #    gameIsOn = True

      # elif(keyboard.read_key() == "n"):
      #    gameIsOn = False