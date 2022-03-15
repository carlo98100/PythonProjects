
import random



global dice


one = ".-------.\n|       |\n|   o   |\n|       |\n|_______|"
two = ".-------.\n|     o |\n|       |\n| o     |\n|_______|"
three = ".-------.\n|     o |\n|   o   |\n| o     |\n|_______|"
four =  ".-------.\n| o   o |\n|       |\n| o   o |\n|_______|"
five =  ".-------.\n| o   o |\n|   o   |\n| o   o |\n|_______|"
six =   ".-------.\n| o   o |\n| o   o |\n| o   o |\n|_______|"

dice = [one, two, three, four, five, six]



print(dice[random.randint(0,5)])
print(dice[random.randint(0,5)])