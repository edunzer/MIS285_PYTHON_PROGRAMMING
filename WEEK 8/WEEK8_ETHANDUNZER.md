## WEEK 8 ETHAN DUNZER

  __8.1__ (Initials)

    *Write a program that gets a string containing a person’s first, middle, and last names, and displays their first, middle, and last initials. For example, if the user enters John William Smith, the program should display J. W. S.*

    ```
      first = str(input("Please enter your First name: "))
      middle = str(input("Please enter your Middle name: "))
      last = str(input("Please enter your Last name: "))

      first_in = first[0] + ". "
      middle_in = middle[0] + ". "
      last_in = last[0] + ". "

      print(first_in, middle_in, last_in)
    ```

  __8.3__ (Date Printer)

    *Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It should print the date in the format March 12, 2018.*

    ```
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
    ```

  __8.9__ (Sentence Capitalizer)

    *Write a program with a function that accepts a string as an argument and returns a copy of the string with the first character of each sentence capitalized. For instance, if the argument is “hello. my name is Joe. what is your name?” the function should return the string “Hello. My name is Joe. What is your name?” The program should let the user enter a string and then pass it to the function. The modified string should be displayed.*

    ```
      def capitalize ():
        user_input = input('Enter a sentence/sentences please:')
        sentences = user_input.split('.')
        for sentence in sentences:
            print (sentence.strip().capitalize()+". ",end='')


      capitalize()
    ```

  __9.2__ (Capitol Quiz)

    *Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values. (Use the Internet to get a list of the states and their capitals.) The program should then randomly quiz the user by displaying the name of a state and asking the user to enter that state’s capital. The program should keep a count of the number of correct and incorrect responses. (As an alternative to the U.S. states, the program can use the names of countries and their capitals.)*

    ```
    import random

    dictonary={
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona':'Phoenix',
        'Arkansas':'Little Rock',
        'California': 'Sacramento',
        'Colorado':'Denver',
        'Connecticut':'Hartford',
        'Delaware':'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinios': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Monies',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'St. Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Neveda': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhoda Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }


    states = list(dictonary.keys())
    points = 0

    print ('US states and Capitals Game. 5 rounds. Enter the word "exit" to quit the game.')

    for i in range(5):
        state = random.choice(states)
        capital = dictonary[state]
        user_input = input('What is the capital of %s?'%state )
        if user_input.lower() == 'exit':
            break
        elif user_input.title() == capital:
            points += 1
            print('Correct! Your score is %d' %points)
        else:
            print('Incorrect. The capital of {} is {}.'.format(state,capital))

    print('Your final score is %d, thank you.' %points)
    ```

  __9.3__ (File Encryption and Decryption)

    *Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:*

      `codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .}`

    *Using this example, the letter A would be assigned the symbol %, the letter a would be assigned the number 9, the letter B would be assigned the symbol @, and so forth.*

    *The program should open a specified text file, read its contents, then use the dictionary to write an encrypted version of the file’s contents to a second file. Each character in the second file should contain the code for the corresponding character in the first file.*

    *Write a second program that opens an encrypted file and displays its decrypted contents on the screen.*

    ```
    code = {"A":"T","a":"T","B":"D","b":"D","C":"L","c":"L","D":"O","d":"O","E":"F","e":"F","F":"A","f":"A","G":"G","g":"G","H":"J","h":"J","I":"K","i":"K","J":"R","j":"R","K":"I","k":"I","L":"C","l":"C","M":"V","m":"V","N":"P","n":"P","O":"W","o":"W","P":"U","p":"U","Q":"X","q":"X","R":"Y","r":"Y","S":"B","s":"B","T":"E","t":"E","U":"Z","u":"Z","V":"Q","v":"Q","W":"S","w":"S","X":"N","x":"N","Y":"M","y":"M","Z":"H","z":"H"}

    def encrypt(sentence, code):
        result = ''
        for letter in sentence:
            if letter in code:
                result = result + code[letter]
            else:
                result = result + letter
        return result
    user_input = input('Please enter your sentence: ')

    print(encrypt(user_input, code))
    ```

  __9.5__ (Word Frequency)

    *Write a program that reads the contents of a text file. The program should create a dictio-nary in which the keys are the individual words found in the file and the values are the number of times each word appears. For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. The program should either display the frequency of each word or create a second file containing a list of each word and its frequency.*

    ```
    def main():
      text = open("text.txt", "r")
      d = dict()

      for line in text:

          line = line.strip()
          line = line.replace('.','')
          line = line.replace(',','')
          line = line.lower()
          words = line.split(" ")

          for word in words:
              if word in d:
                  d[word] = d[word] + 1
              else:
                  d[word] = 1

      for key in list(d.keys()):
          print(key, ":", d[key])

    main()
    ```

  __9.9__ (Blackjack Simulation)

    *Previously in this chapter you saw the card_dealer.py program that simulates cards being dealt from a deck. Enhance the program so it simulates a simplified version of the game of Blackjack between two virtual players. The cards have the following values:*

    *Numeric cards are assigned the value they have printed on them. For example, the value of the 2 of spades is 2, and the value of the 5 of diamonds is 5.*

      `Jacks, queens, and kings are valued at 10.`
      `Aces are valued at 1 or 11, depending on the player’s choice.`

    *The program should deal cards to each player until one player’s hand is worth more than 21 points. When that happens, the other player is the winner. (It is possible that both players’ hands will simultaneously exceed 21 points, in which case neither player wins.) The program should repeat until all the cards have been dealt from the deck.*

    *If a player is dealt an ace, the program should decide the value of the card according to the following rule: The ace will be worth 11 points, unless that makes the player’s hand exceed 21 points. In that case, the ace will be worth 1 point.*

    ```
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
    ```
