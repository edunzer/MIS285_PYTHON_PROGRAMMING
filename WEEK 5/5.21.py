## ROCK PAPER SCISSORS GAME
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
