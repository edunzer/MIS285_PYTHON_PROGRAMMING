## LINE NUMBERS

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
