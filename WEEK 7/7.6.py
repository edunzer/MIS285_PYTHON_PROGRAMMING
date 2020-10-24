## LARGER THAN n

list_name = [1,2,3,4,5,6,7,8,9,10]
number_input = 4

def function(list, number):
    print(list)
    for num in list:

        if num > number:
            print(num)
        else:
            "ERROR"

function(list_name, number_input)
