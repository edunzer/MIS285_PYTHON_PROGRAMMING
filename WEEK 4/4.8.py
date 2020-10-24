## SUM OF NUMBERS

num_list = []

num_input = int(input("Enter a positive numbers: "))
num_list.append(num_input)

while (num_input % 2) == 0:

    num_input = int(input("next: "))
    num_list.append(num_input)

if (num_input % 2) != 0:

    num_list.remove(num_input)
    total = sum(num_list)
    print("Sum of all the numbers: ", total)
