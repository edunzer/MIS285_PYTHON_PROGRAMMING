## WEEK 2 ETHAN DUNZER

  __3.1__

    *Write a program that asks the user for a number in the range of 1 through 7. The program should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display an error message if the user enters a number that is outside the range of 1 through 7.*

    ```
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
    ```

  __3.2__ (Age Classifier)

    *Write a program that asks the user to enter a person’s age. The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult. Following are the guidelines:*
      `If the person is 1 year old or less, he or she is an infant.`
      `If the person is older than 1 year, but younger than 13 years, he or she is a child.`
      `If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.`
      `If the person is at least 20 years old, he or she is an adult.`

    ```
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
    ```

  __3.3__ (Color Mixer)

    *The colors red, blue, and yellow are known as the primary colors because they cannot be made by mixing other colors. When you mix two primary colors, you get a secondary color, as shown here:*
      `When you mix red and blue, you get purple.`
      `When you mix red and yellow, you get orange.`
      `When you mix blue and yellow, you get green.`

    ```
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
    ```

  __3.4__ (Book Club Points)

    *Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:*
      `If a customer purchases 0 books, he or she earns 0 points.`
      `If a customer purchases 2 books, he or she earns 5 points.`
      `If a customer purchases 4 books, he or she earns 15 points.`
      `If a customer purchases 6 books, he or she earns 30 points.`
      `If a customer purchases 8 or more books, he or she earns 60 points.`

    ```
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
    ```

  __3.5__ (Shipping Charges)

    *Write a program that asks the user to enter the weight of a package then displays the shipping charges.*
    *The Fast Freight Shipping Company charges the following rates:*
      `Weight of Package Rate per pound`
      `2 pounds or less $1.50`
      `Over 2 pounds but not more than 6 pounds $3.00`
      `Over 6 pounds but not more than 10 pounds $4.00`
      `Over 10 pounds $4.75`

    ```
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
    ```

  __3.6__ (Turtle Graphics: Hit the Target Modification)

    *Enhance the hit_the_target.py program that you saw in Program 3-9 so that, when the projectile misses the target, it displays hints to the user indicating whether the angle and/or the force value should be increased or decreased. For example, the program should display messages such as 'Try a greater angle' and 'Use less force.'*
