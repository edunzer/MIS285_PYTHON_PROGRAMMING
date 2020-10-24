## WEEK 8 ETHAN DUNZER

  __8.1__ (Initials)

    *Write a program that gets a string containing a person’s first, middle, and last names, and displays their first, middle, and last initials. For example, if the user enters John William Smith, the program should display J. W. S.*

  __8.3__ (Date Printer)

    *Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It should print the date in the format March 12, 2018.*

  __8.9__ (Sentence Capitalizer)

    *Write a program with a function that accepts a string as an argument and returns a copy of the string with the first character of each sentence capitalized. For instance, if the argument is “hello. my name is Joe. what is your name?” the function should return the string “Hello. My name is Joe. What is your name?” The program should let the user enter a string and then pass it to the function. The modified string should be displayed.*

  __9.2__ (Capitol Quiz)

    *Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values. (Use the Internet to get a list of the states and their capitals.) The program should then randomly quiz the user by displaying the name of a state and asking the user to enter that state’s capital. The program should keep a count of the number of correct and incorrect responses. (As an alternative to the U.S. states, the program can use the names of countries and their capitals.)*

  __9.3__ (File Encryption and Decryption)

    *Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:*

      `codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .}`

    *Using this example, the letter A would be assigned the symbol %, the letter a would be assigned the number 9, the letter B would be assigned the symbol @, and so forth.*

    *The program should open a specified text file, read its contents, then use the dictionary to write an encrypted version of the file’s contents to a second file. Each character in the second file should contain the code for the corresponding character in the first file.*

    *Write a second program that opens an encrypted file and displays its decrypted contents on the screen.*

  __9.5__ (Word Frequency)

    *Write a program that reads the contents of a text file. The program should create a dictio-nary in which the keys are the individual words found in the file and the values are the number of times each word appears. For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. The program should either display the frequency of each word or create a second file containing a list of each word and its frequency.*

  __9.9__ (Blackjack Simulation)

    *Previously in this chapter you saw the card_dealer.py program that simulates cards being dealt from a deck. Enhance the program so it simulates a simplified version of the game of Blackjack between two virtual players. The cards have the following values:*

    *Numeric cards are assigned the value they have printed on them. For example, the value of the 2 of spades is 2, and the value of the 5 of diamonds is 5.*

      `Jacks, queens, and kings are valued at 10.`
      `Aces are valued at 1 or 11, depending on the player’s choice.`

    *The program should deal cards to each player until one player’s hand is worth more than 21 points. When that happens, the other player is the winner. (It is possible that both players’ hands will simultaneously exceed 21 points, in which case neither player wins.) The program should repeat until all the cards have been dealt from the deck.*

    *If a player is dealt an ace, the program should decide the value of the card according to the following rule: The ace will be worth 11 points, unless that makes the player’s hand exceed 21 points. In that case, the ace will be worth 1 point.*
