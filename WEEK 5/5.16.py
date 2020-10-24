## ODD/EVEN COUNTER

import random

def generated_random_num():
    random_num = random.randint(1,10)
    return random_num

def even_check(number):
    if (number%2)==0:
        return True
    return False

def printResults(even_num, odd_num):
    print(even_num, "were even.")
    print(odd_num, "were odd.")


def num_list():
    even_num = 0
    odd_num = 0

    for x in range(1,101):
        random_num = generated_random_num()
        print(random_num, end="-")
        if (even_check(random_num)):
            even_num +=1
        else:
            odd_num = odd_num +1
    print()
    printResults(even_num, odd_num)

num_list()
