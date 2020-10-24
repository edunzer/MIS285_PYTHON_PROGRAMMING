# Age classifier

user_age = int(input("Please enter your age:"))

def check_run(user_age):
    if type(user_age) == int and user_age > 0:
        return(classification(user_age))
    else:
        return("ERROR, You did not enter in a number between 0 - ℝ ")

def classification(user_age):
    if int(user_age) in range(0,1):
        return "infant"
    elif int(user_age) in range(2,12):
        return "child"
    elif int(user_age) in range(13,19):
        return "teenager"
    elif int(user_age) in range(20,150):
        return "adult"
    else:
        return "ERROR",user_age


print(check_run(user_age))
