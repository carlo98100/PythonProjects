import datetime


global player_Name
global player_BirthDate

print("Welcome to \"Guess the number\"!")
player_Name = input("Please type your full name [Firstname] [Lastname]:\n")

player_BirthDate = input("Great, now we need to confirm that you are over 18 years old, So please insert your birth date in following format [yyyy:mm:dd]:\n")

date_Format = "yyyy:mm:dd"

try:
    
   # formatting the date using strptime() function
   dateObject = datetime.datetime.strptime(player_BirthDate, date_Format)
   print(dateObject)

# If the date validation goes wrong
except ValueError:

   # printing the appropriate text if ValueError occurs
   print("Incorrect data format, should be YYYYMMDD")