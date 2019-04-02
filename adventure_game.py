import time
import random

list = []
weapons = ["Sword of Swordness", "Hammer of Hammering with Hammering Action",
          "Glitter Bomb of Sparklesplosion"]
creatures = ["Larry the Unicorn", "Carrot Top", "Goldilocks"]
random_creature = random.choice(creatures)
random_weapon = random.choice(weapons)


def print_pause(text):
    time.sleep(0)
    print(text)


def valid_input(prompt):
    while True:
        response = input(prompt)
        if '1' in response:
            break
        elif '2' in response:
            break
        else:
            print_pause("(Please enter 1 or 2.)")
    return response

def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that " + random_creature + " is "
                "somewhere around here, and has been terrifying "
                "the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")


def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    response = valid_input("What would you like to do?\n")
    if '1' in response:
        house()
    elif '2' in response:
        cave()


def cave():
    if "weapon" in list:
        print_pause("You enter the cave.")
        print_pause("It is empty aside from a few bats and "
                    "rats so you return to the field.")
    else:
        print_pause("You slowly enter the cave.")
        print_pause("You see something shining.")
        print_pause("It is the " + random_weapon + "!")
        print_pause("You pick up the " + random_weapon +
                    " and walk back to the field.")
        list.append("weapon")
    field()


def house():
    if "weapon" in list:
        print_pause("You approach the house and knock.")
        print_pause(random_creature + " answers!")
        print_pause(random_creature + " begins to charge!")
        print_pause("You pull out your " + random_weapon +
                    " and " + random_creature + " begins to cry.")
        fight_choice()
        end_game()

    else:
        print_pause("You approach the house and knock.")
        print_pause(random_creature + " answers!")
        print_pause(random_creature + " begins to charge!")
        print_pause("You run away in fear and return to the field.")
        field()


def fight_choice():
    response = valid_input("Enter 1 if you want to hug.\n"
                           "Enter 2 if you want to fight.\n")
    if response == '1':
        print_pause("You throw down your weapon and hug "
                    + random_creature + ", making a new "
                    "friend and healing loneliness.")
        list.append("friend")

    if response == '2':
        print_pause("You use the " + random_weapon + " on "
                    + random_creature + " and they run away "
                    "in abject terror, injured to near death.")
        print_pause("You feel lonely and full of remorse.")
        list.append("enemy")

def end_game():
    if "weapon" in list and "friend" in list:
        print_pause("You've won the game! You made a new friend "
                    "and can now live happily ever after.")
    elif "weapon" in list and "enemy" in list:
        print_pause("GAME OVER")
    print_pause("Do you want to play again?")
    response = valid_input("Enter 1 if you want to play again.\n"
                           "Enter 2 if you want to exit.\n")
    if response == '1':
        print_pause("Alright! Let's play again.\n")
        del list[:]

        play_game()
        print_pause("Thanks for playing, have a great life!")


def play_game():
    intro()
    field()

play_game()
