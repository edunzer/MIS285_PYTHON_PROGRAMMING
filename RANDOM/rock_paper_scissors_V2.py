import random

def RPS():
    print("You are playing Rock Paper Scissors")
    comp_possible  = 1,2,3
    score = [0,0]
    flag = 0
    while True:
        print("Enter your choice:")
        while True:
            choice = input('->')
            if choice == 'r' or choice == 'R' or choice == 'Rock' or choice == 'rock' or choice == '1':
                choice_identifier  = 1
                break
            elif choice == 'S' or choice == 's' or choice == 'Scissors' or choice == 'scissors' or choice == '2':
                choice_identifier =  2
                break
            elif choice == 'P' or choice == 'p' or choice == 'Paper' or choice == 'paper' or choice == '3':
                choice_identifier =  3
                break
            else:
                print('That\'s not an option in this game :)')
                print('Try again:')
                continue

        comp_choice = random.choice(comp_possible)
        if choice_identifier == comp_choice:
            print('It\'s a draw!')
            score[0] = score[0] + 1
            score[1] = score[1] + 1
        elif (choice_identifier == 1 and comp_choice == 2) or (choice_identifier == 2 and comp_choice == 3) or (choice_identifier == 3 and comp_choice == 1):
            print('You win!')
            score[0] = score[0] + 1
        else:
            print('You lose...')
            score[1] = score[1] + 1


        while True:
            answer = input('Play another round?')
            if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes' or answer == 'ye' or answer == 'Ye' or answer == 'sure' or answer == 'Sure':
                print(' Current score: You - ',score[0],' Computer - ',  score[1])
                flag = 0
                break
            elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No' or answer == 'nah' or answer == 'Nah':
                print('Thanks for playing! Final score: You - ',score[0],' Computer - ',  score[1])
                flag = 1
                break
            else:
                print('Yay or nay...')
                continue
        if flag == 0:
            continue
        else:
            break

RPS()
