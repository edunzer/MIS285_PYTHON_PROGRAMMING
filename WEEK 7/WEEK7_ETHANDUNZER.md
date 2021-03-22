## WEEK 7 ETHAN DUNZER

__7.3__ (Rainfall Statistics)
  *Design a program that lets the user enter the total rainfall for each of 12 months into a list. The program should calculate and display the total rainfall for the year, the average monthly rainfall, the months with the highest and lowest amounts.*

  ```
  import sys

    def main():
        month_names = ['January' ,'Febuary' ,'March' ,'April' ,'May' ,'June' ,'July' ,'August' ,'September' ,'Ocotber' ,'November' ,'December']

        num_months = 12
        rain_list = []
        count = 0

        while count <= num_months:
            count += 1

            for month in month_names:
                monthly_rain = float(input("Please enter the rainfall amount for " + month + ": "))
                
                rain_list.append(monthly_rain)
                count += 1

        if count > 12:
            total_rain = sum(rain_list)
            average_rain = total_rain / len(rain_list)
            max_rain = max(rain_list)
            min_rain = min(rain_list)
            print('_'*75)
            print('Total:',total_rain,'\n', 'Average:',average_rain,'\n', 'Highest:',max_rain,'\n', 'Lowest:',min_rain)
            print('_'*75)
            sys.exit()

        else:
            print("ERROR")
            sys.exit()

    main()
  ```

__7.6__ (Larger Than n)
  *In a program, write a function that accepts two arguments: a list, and a number n. Assume that the list contains numbers. The function should display all of the numbers in the list that are greater than the number n.*

  ```
  list_name = [1,2,3,4,5,6,7,8,9,10]
  number_input = 4

  def function(list, number):
      print(list)
      for num in list:

          if num > number:
              print(num)
          else:
              "ERROR"

  function(list_name, number_input)
  ```

__7.12__ (Prime Number Generation)
  *A positive integer greater than 1 is said to be prime if it has no divisors other than 1 and itself. A positive integer greater than 1 is composite if it is not prime. Write a program that asks the user to enter an integer greater than 1, then displays all of the prime numbers that are less than or equal to the number entered. The program should work as follows:*
    `Once the user has entered a number, the program should populate a list with all of the integers from 2 up through the value entered.`
    `The program should then use a loop to step through the list. The loop should pass each element to a function that displays the element whether it is a prime number.`

  ```
  def function():
    lower = 1
    upper = int(input("Please enter in a number greater than 0: "))
    for num in range(lower, upper + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num)

  function()
  ```

__7.14__ (Expense Pie Chart)
  *Create a text file that contains your expenses for last month in the following categories: Rent Gas Food Clothing Car payment Misc Write a Python program that reads the data from the file and uses matplotlib to plot a pie chart showing how you spend your money.*

  ```
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
  ```

