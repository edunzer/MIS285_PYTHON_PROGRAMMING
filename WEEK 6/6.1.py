## FILE DISPLAY

def main():
    infile = open('numbers.txt', 'r')
    file_contents = infile.read()

    infile.close()
    print(file_contents)

main()
