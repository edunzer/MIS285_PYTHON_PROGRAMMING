## BLACKJACK SIMULATION

import os
import random

# -------------------- DECK LIST with USER DECK NUMBER CHOICE ------------------------
decks = input("How many decks would you like to use?: ")
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

# -------------------- SCORE VARIABLE HOLDS ------------------------
wins = 0
losses = 0

# -------------------- WINDOW CLEAR ------------------------
def clear():

    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

# -------------------- PLAY AGAIN ASK ------------------------
def play_again():

    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Game Ended!")
        exit()

# -------------------- CARD DEAL FUNCTION ------------------------
def deal(deck):

    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

# -------------------- HIT FUNCTION ------------------------
def hit(hand):

    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

# -------------------- COUNT FUNCTION ------------------------
def total(hand):

    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

# -------------------- RESULTS CHART ------------------------
def print_results(dealer_hand, player_hand):

    clear()

    print("\n    WELCOME TO BLACKJACK!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

# -------------------- WIN CHECK ------------------------
def blackjack(dealer_hand, player_hand):

    global wins
    global losses

    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
        play_again()

# -------------------- SCORE COUNTER ------------------------
def score(dealer_hand, player_hand):

    global wins
    global losses

    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        wins += 1
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry. You busted. You lose.\n")
        losses += 1
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Dealer busts. You win!\n")
        wins += 1
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
        losses += 1
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print ("Congratulations. Your score is higher than the dealer. You win\n")
        wins += 1

# -------------------- MAIN GAME FUNCTION ------------------------
def game():

    global wins
    global losses

    user_input = 0
    clear()

    print("\n    WELCOME TO BLACKJACK!\n")
    print("-"*30)
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s" % (wins, losses))
    print("-"*30)

    dealer_hand = deal(deck)
    player_hand = deal(deck)

    print ("The dealer is showing a " + str(dealer_hand[0]))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

    blackjack(dealer_hand, player_hand)

    quit = False
    while not quit:
        user_input = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if user_input == 'h':
            hit(player_hand)
            print(player_hand)
            print("Hand total: " + str(total(player_hand)))
            if total(player_hand)>21:
                print('You busted')
                losses += 1
                play_again()
        elif user_input == 's':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Dealer busts, you win!')
                    wins += 1
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif user_input == "q":
            print("Game Ended!")
            quit = True
            exit()



game()
