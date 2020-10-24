## DATE PRINTER

def format_change(user_input):
    user_input_values = user_input.split("/")
    user_month = user_input_values[0]
    user_day = user_input_values[1]
    user_year = user_input_values[2]

    return user_month, user_day, user_year

def date_change():
    user_input = input("Please enter a date in the form mm/dd/yyyy: ")
    monthNames = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    user_month, user_day, user_year = format_change(user_input)

    month_num = int(user_month) - 1
    month_change = monthNames[month_num]

    new_format = month_change + " " + user_day + ", " + user_year

    print("You typed " + user_input, "and was changed to " + new_format, sep="\n")

date_change()
