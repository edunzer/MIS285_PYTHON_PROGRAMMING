## BUDGET ANALYSIS (v3)

import sys

stored = {}
total_list = [0]
budget_store = [0]

def chart(stored):
    print('ITEM \t\t COST')
    print('-------------------------')
    for item in stored:
        print(item, '\t\t',stored[item])

def item_add(item_input, cost_input):

    if item_input.isalpha() == True and cost_input >= 0:
        stored[item_input] = cost_input

        print('___________________________________________________________________________')
        user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()
        print('___________________________________________________________________________')

        print(user_input)
        loop(user_input)
    else:
        print("ERROR1")

def loop(user_input):

    while user_input == 'yes':
        print('___________________________________________________________________________')
        item_input, cost_input = input("Please enter the item to add to your budget and the cost of that item: ").split()
        print('___________________________________________________________________________')

        item_input = str(item_input).lower()
        cost_input = int(cost_input)

        chart(stored)
        item_add(item_input, cost_input)
    else:
        chart(stored)
        budget_check()

def budget(budget_store):
    print('___________________________________________________________________________')
    budget_input = int(input("Please enter your budget for this month: "))
    print("You entered: ",budget_input)
    print('___________________________________________________________________________')

    budget_store.append(int(budget_input))

    print('___________________________________________________________________________')
    user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()
    print("You entered: ",user_input)
    print('___________________________________________________________________________')
    loop(user_input)

def budget_check():
    for val in stored.values():
        total_list.append(int(val))
    for val in stored.values():
        total = sum(total_list)
        total = int(total)
        print('-------------------------')
        print("Total: ",'\t', total)
        print('-------------------------')
        break

    budget_store.remove(int(0))

    if budget_store[0] < total:
        difference = total - budget_stor[0]
        print("Over budget by: ", difference)
        sys.exit()
    elif budget_store[0] > total:
        difference = budget_store[0] - total
        print("Under budget by: ", difference)
        sys.exit()
    else:
        print("ERROR3")


budget(budget_store)
