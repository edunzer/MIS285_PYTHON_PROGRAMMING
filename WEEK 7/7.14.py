## EXPENSE PIE CHART

#import matplotlib.pyplot as plt

def read():
    infile = open('expenses.txt', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    line6 = infile.readline()
    line7 = infile.readline()
    line8 = infile.readline()
    line9 = infile.readline()
    line10 = infile.readline()
    line11 = infile.readline()
    line12 = infile.readline()
    infile.close()

    print('_'*75)

    infile = open('expenses.txt', 'r')
    name = infile.readline().rstrip('\n')

    while name != "":
        price = infile.readline().rstrip('\n')

        print(name, price)
        name = infile.readline().rstrip('\n')

    infile.close()

    print('_'*75)


    my_data = [line2, line4, line6, line8, line10, line12]
    my_labels = line1, line3, line5, line7, line9, line11
    plt.pie(my_data,labels=my_labels,autopct='%1.1f%%')
    plt.title('Expenses')
    plt.axis('equal')
    plt.show()


read()
