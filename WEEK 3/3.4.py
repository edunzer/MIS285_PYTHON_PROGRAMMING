# Book club points
user_input = int(input("Please enter the number of books that have been purchased this month: "))

user_points = [0]
user_points = list(map(int, user_points))

def point_calculator(user_input):
    if user_input>=2 and user_input <= 3:
        for num in user_points:
            user_points[0] += 5
            break
        print("You will get", user_points, "points.")
    elif user_input >=4 and user_input <= 5:
        for num in user_points:
            user_points[0] += 15
            break
        print("You will get", user_points, "points.")
    elif user_input >=6 and user_input <= 7:
        for num in user_points:
            user_points[0] += 30
            break
        print("You will get", user_points, "points.")
    elif user_input >=8:
        for num in user_points:
            user_points[0] += 60
            break
        print("You will get", user_points, "points.")
    else:
        print("ERROR 1")


print(point_calculator(user_input))

option_select = str(input("Would you like to see how many points you have in total? Yes or No: ")).lower()

if option_select == 'yes' or option_select == 'y':
    print(max(user_points))
elif option_select == 'no' or option_select == 'n':
    print("Okay have a good day.")
else:
    print("ERROR 2")
