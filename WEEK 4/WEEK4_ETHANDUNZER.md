## WEEK 4 ETHAN DUNZER

  __4.2__ (Calories burnt)
    *Calories Burned Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.*

    ```
    per_minute = float(4.2)
    minutes = [10,15,20,25,30]

    for number in minutes:
        print(number*4.2)
    ```

  __4.3__ (Budget Analysis)
    *Write a program that asks the user to enter the amount that he or she has budgeted for a month.*
      `A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total.`
      `When the loop finishes, the program should display the amount that the user is over or under budget.`

    ```
    x = 0
    budget = 0

    budget = input("Please enter your budget:")
    budget = int(budget)
    num = int(input("Please enter money spent (enter 0 to quit): "))

    while num != 0:
      x = x + num
      num = int(input("Please enter money spent (enter 0 to quit): "))

    if x > budget :
      end = x - budget
      print("You went over your budget by: ", end)

    elif x < budget:
      end = budget - x
      print ("You are under budget by: ", end)
    ```

  __4.6__ (Celsius to Fahrenheit Table)
    *Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents. The formula for converting a temperature from Celsius to Fahrenheit is F=95C+32*

    ```
    def conversion():

      print('Celsius\t   Farenheit')
      print('---------------------')

      for c in range (0, 21, +1):
          f = (9 / 5) * c + 32
          print(c, '\t', format(f, '.1f'))

    conversion()
    ```

  __4.8__ (Sum of Numbers)
    *Sum of Numbers Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative number to signal the end of the series. After all the positive numbers have been entered, the program should display their sum.*

    ```
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
    ```

  __4.11__ (Weight Loss)
    *Weight Loss If a moderately active person cuts their calorie intake by 500 calories a day, they can typically lose about 4 pounds a month. Write a program that lets the user enter their starting weight, then creates and displays a table showing what their expected weight will be at the end of each month for the next 6 months if they stay on this diet.*

    ```
    w_start = int(input("Please enter in your start weight: "))

    def chart(w_start):
        print('Month\t   Weight')
        print('----------------')

        for m in range (0, 7, +1):
            w = (w_start-(4*m))
            print(m, '\t', w)

    chart(w_start)
    ```

  __4.18__
