# Dice rolling program
import random


def roll():
    min = 1
    max = 6

    def roll_dice():
        roll_again = "yes"

        while roll_again == "yes" or roll_again == "y":
            print("Rolling the dices...")
            print("The values are....")
            print(random.randint(min, max))

            roll_again = input("Roll the dices again?")

    roll_dice()


roll()
