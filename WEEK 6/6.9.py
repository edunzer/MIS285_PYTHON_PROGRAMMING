## EXCEPTION HANDING

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
