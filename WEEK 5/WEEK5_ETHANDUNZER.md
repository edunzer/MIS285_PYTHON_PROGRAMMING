## WEEK 5 ETHAN DUNZER

  __5.3__ (How much insurance)
    *Many financial experts advise that property owners should insure their homes or buildings for at least 80 percent of the amount it would cost to replace the structure. Write a program that asks the user to enter the replacement cost of a building, then displays the minimum amount of insurance he or she should buy for the property.*

    ```
    import sys
    import time
    import random

    # -------------------- PROGRESS BAR CODE ------------------------
    def updt(total, progress):

        barLength, status = 20, ""
        progress = float(progress) / float(total)
        if progress >= 1.:
            progress, status = 1, "\r\n"
        block = int(round(barLength * progress))
        text = "\r[{}] {:.0f}% {}".format(
            "■" * block + "-" * (barLength - block), round(progress * 100, 0),
            status)
        sys.stdout.write(text)
        sys.stdout.flush()

    random_num = random.randint(10,60)
    runs = random_num # -------------------- TIME SELECT ---------------------------


    user_input = float(input("How much would it cost to re-build your house? -->"))
    calc = user_input * 0.80

    #  ---------------------- PROGRESS BAR -----------------------
    for run_num in range(runs):
        time.sleep(.1)
        updt(runs, run_num + 1)

    print("Here is your recommended insurance amount -->",calc)
    ```

  __5.4__ (Automobile costs)
    *Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. The program should then display the total monthly cost of these expenses, and the total annual cost of these expenses.*

    ```
    print("Please enter in the amounts for the following monthly costs of your vehicle:")

    loan_input = int(input("loan -->"))
    insurance_input = int(input("insurance -->"))
    gas_input = int(input("gas -->"))
    oil_input = int(input("oil -->"))
    tires_input = int(input("tires -->"))
    maintence_input = int(input("maintence -->"))

    monthly_total = loan_input + insurance_input + gas_input + oil_input + tires_input + maintence_input
    print("Here is your monthly total: ",monthly_total)
    annual_total = monthly_total * 12
    print("Here is your annual total: ",annual_total)
    ```

  __5.7__ (Stadium seating)
    *There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10. Write a program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales.*

    ```
    class_a = 20
    class_b = 15
    class_c = 10

    print("Please enter in the number of tickets sold for each class:")
    a_input = int(input("Class A tickets -->"))
    b_input = int(input("Class B tickets -->"))
    c_input = int(input("Class C tickets -->"))

    sold_a = a_input * class_a
    sold_b = b_input * class_b
    sold_c = c_input * class_c

    print("Here is the total for Class A tickets: ", sold_a)
    print("Here is the total for Class B tickets: ", sold_b)
    print("Here is the total for Class C tickets: ", sold_c)
    ```
    
  __5.9__ (Monthly sales tax)
    *A retail company must file a monthly sales tax report listing the total sales for the month, and the amount of state and county sales tax collected. The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter the total sales for the month. From this figure, the application should calculate and display the following:*
      `The amount of county sales tax`
      `The amount of state sales tax`
      `The total sales tax(county plus state)`

    ```
    sales_input = int(input("Please enter in the total amount of sales income for this month -->"))

    state_tax = float(0.05)
    county_tax = float(0.025)

    state_total = sales_input * state_tax
    county_total = sales_input * county_tax
    total_tax = state_total + county_total

    print("Here is your calculated state tax: ",state_total)
    print("Here is your calculated county tax: ",county_total)
    print("Here is your total calculated tax: ", total_tax)
    ```

  __5.11__ (Math quiz)
    *Write a program that gives simple math quizzes. The program should display two random numbers that are to be added, such as:*
      `247 + 129`
    *The program should allow the student to enter the answer. If the answer is correct, a message of congratulations should be displayed. If the answer is incorrect, a message showing the correct answer should be displayed.*

    ```
    import random

    variable_1 = random.randint(1,1000)
    variable_2 = random.randint(1,1000)

    solution = variable_1 + variable_2

    print("What is the answer to this question: ", variable_1, "+", variable_2)
    user_input = int(input("-->"))

    if user_input == solution:
        print("CORRECT!!! good job")
    else:
        print("NOPE!!! sorry wrong answer. The correct answer was: ", solution)
    ```

  __5.16__ (Odd/Even counter)
    *In this chapter, you saw an example of how to write an algorithm that determines whether a number is even or odd. Write a program that generates 100 random numbers and keeps a count of how many of those random numbers are even, and how many of them are odd.*

    ```
    import random

    def generated_random_num():
        random_num = random.randint(1,10)
        return random_num

    def even_check(number):
        if (number%2)==0:
            return True
        return False

    def printResults(even_num, odd_num):
        print(even_num, "were even.")
        print(odd_num, "were odd.")


    def num_list():
        even_num = 0
        odd_num = 0

        for x in range(1,101):
            random_num = generated_random_num()
            print(random_num, end="-")
            if (even_check(random_num)):
                even_num +=1
            else:
                odd_num = odd_num +1
        print()
        printResults(even_num, odd_num)

    num_list()
    ```

  __5.21__ (Rock, Paper, Scissors game)
    *Write a program that lets the user play the game of Rock, Paper, Scissors against the computer. The program should work as follows:*
      `When the program begins, a random number in the range of 1 through 3 is generated. If the number is 1, then the computer has chosen rock. If the number is 2, then the computer has chosen paper. If the number is 3, then the computer has chosen scissors. (Don’t display the computer’s choice yet.)`
      `The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.`
      `The computer’s choice is displayed.`
      `A winner is selected according to the following rules:`
        *If one player chooses rock and the other player chooses scissors, then rock wins. (Rock smashes scissors.)*
        *If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors cut paper.)*
        *If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps rock.)*
        *If both players make the same choice, the game must be played again to determine the winner.*

    ```
    import random
    import sys

    def generate_random_num():
        random_num = random.randint(1,3)
        return random_num

    def get_choice(random_num):
        if random_num == 1:
            computer_choice = "rock"
        elif random_num == 2:
            computer_choice = "paper"
        elif random_num == 3:
            computer_choice = "scissors"
        return computer_choice

    def get_user_choice():
        user_choice = input("Please enter your choice(enter 'end' to stop): ").lower()

        if user_choice.isalpha():
            if user_choice == "exit":
                print("The program has been terminated")
                sys.exit()
            else:
                return user_choice
        else:
            print("That wasnt an option, please try again.")
            get_user_choice()



    def winner_check(computer_choice, user_choice):
        rock_message = "The rock smashes the scissors"
        scissors_message = "Scissors cuts paper"
        paper_message = "Paper wraps rock"
        winner = "no winner"
        message = ""

        if computer_choice == "rock" and user_choice == "scissors":
            winner = "computer"
            message = rock_message
        elif computer_choice == "scissors" and user_choice == "rock":
            winner = "You"
            message = rock_message

        if computer_choice == "scissors" and user_choice == "paper":
            winner = "Computer"
            message = scissors_message
        elif computer_choice == "paper" and user_choice == "scissors":
            winner = "You"
            message = scissors_message

        if computer_choice == "paper" and user_choice == "rock":
            winner = "Computer"
            message = paper_message
        elif computer_choice == "rock" and user_choice == "paper":
            winner = "You"
            message = paper_message

        return winner, message

    def repeat():
        random_num = generate_random_num()
        computer_choice = get_choice(random_num)
        user_choice = get_user_choice()
        print("The computer chooses: ", computer_choice)
        winner, message = winner_check(computer_choice, user_choice)

        if winner != "no winner":
            print(winner, "won(", message, ")")
        return winner

    def main():
        random_num = generate_random_num()
        computer_choice = get_choice(random_num)
        user_choice = get_user_choice()
        print()
        print("The computer chooses: ", computer_choice)
        winner, message = winner_check(computer_choice, user_choice)

        if winner != "no winner":
            print(winner, "won(",message,")")
        while winner == "no winner":
            print("\nYou both chose the same thing")
            winner = repeat()

    main()
    ```
