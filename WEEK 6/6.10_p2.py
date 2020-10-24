## GOLF SCORES (READ PROGRAM)



def read():
    file = open('golf.txt', 'r')
    name = file.readline().rstrip('\n')

    while name != "":
        score = file.readline().rstrip('\n')

        print(name, score)
        name = file.readline().rstrip('\n')

    file.close()

read()
