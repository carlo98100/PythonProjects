import random



global dices


def DrawDice(dice1, dice2) :
    for x in range(5) :
        print(dices[dice1][x] + "   " + dices[dice2][x])


one = [".-------.","|       |","|   o   |","|       |","|_______|"]
two = [".-------.","|     o |","|       |","| o     |","|_______|"]
three = [".-------.","|     o |","|   o   |","| o     |","|_______|"]
four = [".-------.","| o   o |","|       |","| o   o |","|_______|"]
five = [".-------.","| o   o |","|   o   |","| o   o |","|_______|"]
six = [".-------.","| o   o |","| o   o |","| o   o |","|_______|"]


dices = [one, two, three, four, five, six]


DrawDice(random.randint(0,5), random.randint(0,5))
print()