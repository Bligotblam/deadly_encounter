# Deadly Encounter.

# This is a character creation and RPG style fighting scenario. Enjoy!

# Name your character.
q1 = 0
while q1 != "y":
    char_name = input("What would you like your character to be named? ")
    q1 = input("Your character will be named " + char_name + " is that correct? [y/n]? ")

# Picking a character.
q2 = 0
while q2 != "a" and q2 != "b":
    q2 = input("Do you want to: a) Fighter. b) Bard. [a/b]?: ")
    if q2 == "a":
        char_class = 'Fighter'
        print("You chose a Fighter.")
    elif q2 == "b":
        char_class = 'Bard'
        print("You chose a Bard.")


# Checking stats command

def stats(char_name, char_class):
    if char_class == "Fighter":
        print("You are " + char_name)
        print("Your a Fighter :")
        print(" ")
        print("Stats")
        print("STR: 15")
        print("Dex: 14")
        print("Con: 13")
        print("Int: 12")
        print("Wis: 10")
        print("Chr: 8")
    elif char_class == 'Bard':
        print("You are " + char_name)
        print("Your a Bard :")
        print(" ")
        print("Stats")
        print("STR: 15")
        print("Dex: 14")
        print("Con: 13")
        print("Int: 12")
        print("Wis: 10")
        print("Chr: 8")


stats(char_name, char_class)
