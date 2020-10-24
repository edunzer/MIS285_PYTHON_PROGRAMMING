## AVERAGE OF NUMBERS

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
