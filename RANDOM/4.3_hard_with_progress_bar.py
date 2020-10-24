## BUDGET ANALYSIS (v2)

import sys
import time
import random

stored = {}
total_list = [0]
budget_store = [0]

# -------------------- PROGRESS BAR CODE ------------------------
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

random_num = random.randint(10,60)
runs = random_num # -------------------- TIME SELECT ---------------------------

# -------------------- CHART ------------------------
def chart(stored):
    print('ITEM \t\t COST')
    print('-'*25)
    for item in stored:
        print(item, '\t\t',stored[item])

# -------------------- ITEM ADD ------------------------
def item_add(item_input, cost_input):

    if item_input.isalpha() == True and cost_input >= 0:
        stored[item_input] = cost_input

        chart(stored)

        print('_'*75)
        user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()

        print(user_input)
        print('_'*75)

        loop(user_input)

    else:
        print("ERROR1")

# -------------------- CONTINUE ENTER CHECK ------------------------
def loop(user_input):

    while user_input == 'yes' or user_input == 'y':
        print('_'*75)
        item_input, cost_input = input("Please enter the item to add to your budget and the cost of that item: ").split()
        print('_'*75)

        item_input = str(item_input).lower()
        cost_input = float(cost_input)

        #chart(stored)
        item_add(item_input, cost_input)

    if user_input == 'no' or user_input == 'n':
        print('_'*75)
        print("Program ENDED")
        print('_'*75)
        chart(stored)
        budget_check()

    else:
        print('_'*75)
        print("You did not select Yes or No. Program ENDED")
        print('_'*75)
        chart(stored)
        sys.exit()

# -------------------- BUDGET ENTER ------------------------
def budget(budget_store):
    print('_'*75)
    budget_input = input("Please enter your budget for this month: ")
    print("You entered: ","$",budget_input)
    print('_'*75)

    #  ---------------------- INTEGER CHECK -----------------------
    try:
        val = float(budget_input)
        budget_store.append(float(budget_input))

        print('_'*75)
        user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()
        print("You entered: ",user_input)
        print('_'*75)
        loop(user_input)
    except ValueError:
        print("You did no enter an integer. Program ENDED")
        sys.exit()

# -------------------- BUDGET CHECK ------------------------
def budget_check():
    for val in stored.values():
        total_list.append(int(val))
    for val in stored.values():
        total = sum(total_list)
        total = int(total)

        print('-'*25)
        print("Calculating your total")
        print('-'*25)

        #  ---------------------- PROGRESS BAR -----------------------
        for run_num in range(runs):
            time.sleep(.1)
            updt(runs, run_num + 1)

        print('-'*25)
        print("Total: ",'\t', total)
        print('-'*25)
        break
        #  ---------------------- ----------- -----------------------


    budget_store.remove(int(0))

    if budget_store[0] < total:
        difference = total - budget_store[0]
        print("Over budget by: ", difference)
        print('-'*25)
        sys.exit()
    elif budget_store[0] > total:
        difference = budget_store[0] - total
        print("Under budget by: ", difference)
        print('-'*25)
        sys.exit()
    else:
        print("ERROR3")


budget(budget_store)
