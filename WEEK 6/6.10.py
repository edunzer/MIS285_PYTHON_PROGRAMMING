## GOLF SCORES

import sys
import time
import random

stored = {}
value = 0
runs = 50

# -------------------- PROGRESS BAR ------------------------
def updt(total, progress):

    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "■" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()

# -------------------- CONTENT ADD TO FILE ------------------------
def file_add():
    outfile = open('golf.txt', 'a')

    for name in stored:
        outfile.write(str(name) + '\n')
        outfile.write(str(stored[name]) + '\n')
    outfile.close()
    print('_'*75)
    print('Uploading data to golf.txt')
    for run_num in range(runs):
        time.sleep(.1)
        updt(runs, run_num + 1)
    print('Data has been written to golf.txt')
    print('_'*75)
    sys.exit()

# -------------------- CHART ------------------------
def chart(stored):
    print('ITEM \t\t COST')
    print('-'*25)
    for item in stored:
        print(item, '\t\t',stored[item])

# -------------------- PLAYER ADD ------------------------
def player_add(name_add, score_add):
    if name_add.isalpha() == True and score_add > 0:
        stored[name_add] = score_add

        chart(stored)

        print('_'*75)
        user_input = input("Do you want to continue entering players and scores? Enter yes or no: ").lower()
        print(user_input)
        print('_'*75)
        loop(user_input)

    else:
        print("ERROR1")
        print(name_add, score_add)
        print(stored)
        sys.exit()

# -------------------- USER INPUT ASK ------------------------
def loop(user_input):
    while user_input == 'yes' or user_input == 'y':
        print('_'*75)
        name_add, score_add = input("Please enter the name of the player and the score of the player: ").split()
        print('_'*75)

        name_add = str(name_add).lower()
        score_add = int(score_add)

        player_add(name_add, score_add)

    if user_input == 'no' or user_input == 'n':
        print('_'*75)
        print('Program ENDED')
        print('_'*75)
        chart(stored)
        file_add()
        sys.exit()

    else:
        print('_'*75)
        print("You did not select Yes or No. Program ENDED")
        print('_'*75)
        chart(stored)
        sys.exit()

# -------------------- PLAYER COUNT ------------------------
def player_count():
    player_num = int(input("How many players are in the tournament: "))
    if player_num > 0:
        user_input = 'yes'
        loop(user_input)
    else:
        print('ERROR You did not enter a number ')
        player_count()

player_count()
