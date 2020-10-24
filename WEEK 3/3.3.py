# Color mixer

user_input = str(input("Please enter in a secondary color (purple, orange, green) you would like to make: ")).lower()

complete_colors = {
    'purple':['red','blue'],
    'orange':['red','yellow'],
    'green':['blue','yellow']
}

def color_mixer(user_input):
    if user_input == 'purple':
        print("To make purple you need ", complete_colors[user_input])
    elif user_input == 'orange':
        print("To make orange you need ", complete_colors[user_input])
    elif user_input == 'green':
        print("To make green you need ", complete_colors[user_input])

    else:
        return "ERROR"


print(color_mixer(user_input))
