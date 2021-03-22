## WEEK 6 ETHAN DUNZER

  __6.1__ (File Display)
    *Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk. Write a program that displays all of the numbers in the file.*

    ```
    def main():
      infile = open('numbers.txt', 'r')
      file_contents = infile.read()

      infile.close()
      print(file_contents)

    main()
    ```    

  __6.3__ (Line Numbers)
    *Write a program that asks the user for the name of a file. The program should display the contents of the file with each line preceded with a line number followed by a colon. The line numbering should start at 1.*

    ```
    def main():
      userinput = input('Please enter a name of a file -->')

      print()

      read_file = open(userinput, "r")
      line = read_file.readline()

      line_num = 1

      while line != "":
          print(str(line_num) + ":", line.rstrip("\n"))
          line = read_file.readline()
          line_num = line_num + 1

    main()
    ```    

  __6.6__ (Average of Numbers)
    *Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk. Write a program that calculates the average of all the numbers stored in the file.*

    ```
    def main():
      try:
          file = open('numbers.txt', 'r')
      except Exception as error:
          print('File not found:', error)
      else:
          total = 0
          number_lines = 0
          line = file.readline()

          while line != '':
              number_lines += 1
              total += int(line)
              line = file.readline()

          average = total / number_lines

          print('The average is:', average)

    main()
    ```    

  __6.9__ (Exception Handing)
    *Modify the program that you wrote for Exercise 3 (6-6) so it handles the following exceptions:*
      ` It should handle any IOError exceptions that are raised when the file is opened and data is read from it.`
      ` It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number.`

    ```
    def main():
      try:
          file = open('numbers.txt', 'r')
          total = 0
          number_lines = 0
          num = file.readline()

          while num != '':
              number_lines += 1
              total += int(line)
              num = file.readline()

          average = total / number_lines
      except IOError as error:
          print('An IOError has occured:', error)
      except ValueError as error:
          print('A ValueError has occured:', error)
      else:
          print('The average is:', average)
      finally:
          print('END')

    main()
    ```    

  __6.10__ (Golf Scores)
    *The Springfork Amateur Golf Club has a tournament every weekend. The club president has asked you to write two programs:*
      `A program that will read each player’s name and golf score as keyboard input, then save these as records in a file named golf.txt. (Each record will have a field for the player’s name and a field for the player’s score.)`
      `A program that reads the records from the golf.txt file and displays them.`

    ```
    import sys
    import time
    import random

    stored = {}
    value = 0
    runs = 50

    # -------------------- PROGRESS BAR ------------------------
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

    # -------------------- CONTENT ADD TO FILE ------------------------
    def file_add():
        outfile = open('golf.txt', 'a')

        for name in stored:
            outfile.write(str(name) + '\n')
            outfile.write(str(stored[name]) + '\n')
        outfile.close()
        print('_'*75)
        print('Uploading data to golf.txt')
        for run_num in range(runs):
            time.sleep(.1)
            updt(runs, run_num + 1)
        print('Data has been written to golf.txt')
        print('_'*75)
        sys.exit()

    # -------------------- CHART ------------------------
    def chart(stored):
        print('ITEM \t\t COST')
        print('-'*25)
        for item in stored:
            print(item, '\t\t',stored[item])

    # -------------------- PLAYER ADD ------------------------
    def player_add(name_add, score_add):
        if name_add.isalpha() == True and score_add > 0:
            stored[name_add] = score_add

            chart(stored)

            print('_'*75)
            user_input = input("Do you want to continue entering players and scores? Enter yes or no: ").lower()
            print(user_input)
            print('_'*75)
            loop(user_input)

        else:
            print("ERROR1")
            print(name_add, score_add)
            print(stored)
            sys.exit()

    # -------------------- USER INPUT ASK ------------------------
    def loop(user_input):
        while user_input == 'yes' or user_input == 'y':
            print('_'*75)
            name_add, score_add = input("Please enter the name of the player and the score of the player: ").split()
            print('_'*75)

            name_add = str(name_add).lower()
            score_add = int(score_add)

            player_add(name_add, score_add)

        if user_input == 'no' or user_input == 'n':
            print('_'*75)
            print('Program ENDED')
            print('_'*75)
            chart(stored)
            file_add()
            sys.exit()

        else:
            print('_'*75)
            print("You did not select Yes or No. Program ENDED")
            print('_'*75)
            chart(stored)
            sys.exit()

    # -------------------- PLAYER COUNT ------------------------
    def player_count():
        player_num = int(input("How many players are in the tournament: "))
        if player_num > 0:
            user_input = 'yes'
            loop(user_input)
        else:
            print('ERROR You did not enter a number ')
            player_count()

    player_count()

    ```  
    Part 2

    ```
    def read():
      file = open('golf.txt', 'r')
      name = file.readline().rstrip('\n')

      while name != "":
          score = file.readline().rstrip('\n')

          print(name, score)
          name = file.readline().rstrip('\n')

      file.close()

    read()  
    ```