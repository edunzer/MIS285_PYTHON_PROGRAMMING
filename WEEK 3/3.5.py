# Shipping charges

def lbs(weight):
    if weight <= 2:
        cost = weight * 1.50
        print("Your package will cost: $",cost)
    elif weight >= 2 and weight <= 6:
        cost = weight * 3.00
        print("Your package will cost: $",cost)
    elif weight >= 6 and weight <= 10:
        cost = weight * 4.00
        print("Your package will cost: $",cost)
    elif weight >= 10:
        cost = weight * 4.00
        print("Your package will cost: $",cost)
    else:
        print("ERROR, You didnt enter in a number.")

def kg(weight):
    if weight <= 0.9:
        cost = weight * 1.50
        print("Your package will cost: $",cost)
    elif weight >= 0.9 and weight <= 2.7:
        cost = weight * 3.00
        print("Your package will cost: $",cost)
    elif weight >= 2.7 and weight <= 4.5:
        cost = weight * 4.00
        print("Your package will cost: $",cost)
    elif weight >= 4.5:
        cost = weight * 4.00
        print("Your package will cost: $",cost)
    else:
        print("ERROR, You didnt enter in a number.")


choice = str(input("Would you like to use lbs or kg for weight? ")).lower()
weight = float(input("Please enter the weight of your package: "))

if choice == 'lbs':
    print(lbs(weight))
elif choice == 'kg':
    print(kg(weight))
