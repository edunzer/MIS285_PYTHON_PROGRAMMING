#Day input program

user_input = int(input("Please enter a number between 1 and 7:"))

days = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wensday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    7 : 'Sunday'}

if user_input >= 1 and user_input <= 7:
    print(days[user_input])
else:
    print("Error, you didnt type in a number between 1 and 7!")
