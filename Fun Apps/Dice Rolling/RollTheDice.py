import random

def roll(sides):
    num_rolled = random.randint(1, sides)
    return num_rolled

def main():
    rolling = True
    while rolling:
        sides = raw_input("Choose you dice: 3 sides=3, 6 sides=6(default), 12 sides=12")
        if sides == "":
            sides="6"
        roll_again = raw_input("Ready to roll? Enter=Roll. Q=Quit. ")
        if roll_again.lower() !="q":
            num_rolled = roll(int(sides))
            print "You rolled a", num_rolled
        else:
            rolling = False
    print "Thanks for playing."

main()