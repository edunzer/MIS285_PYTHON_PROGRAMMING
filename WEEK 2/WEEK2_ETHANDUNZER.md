## WEEK2_ETHANDUNZER

  __2.1__

    *Write a program that displays the following information*
      `Your name`
      `Your address`
      `Your phone number`
      `Your college major`

      name = "My name is Ethan Dunzer. ";
      address = "I live at *******************. ";
      phone = "My phone number is *************.";
      major = "Im studing Information Technology.";

      print(name,'\n', address,'\n', phone,'\n', major);

    ```
    name = "My name is Ethan Dunzer. " ;
    address = "I live at *******************. ";
    phone = "My phone number is *************.";
    major = "Im studing Information Technology.";

    print(name,'\n', address,'\n', phone,'\n', major);
    ```

  __2.3__

    *One acre of land is equiveland to 43,560 square feet. Write a program that asks the use to enter the total square feet in a tract of land and calculates the number of acres in the tract.*
      `Hint: divide the amout entered by 43,560 to get the number of acres.`

      print("Please enter the total square feet you want to convert into acres");
      square_ft_input = int(input());
      x = 43560;

      acre_output = (square_ft_input / x);
      print(square_ft_input, 'is ', acre_output, 'acres');

    ```
    print("Please enter the total square feet you want to convert into acres");
    square_ft_input = int(input());
    x = 43560;

    acre_output = (square_ft_input / x);
    print(square_ft_input, 'is ', acre_output, 'acres');
    ```

  __2.7__

    *A car's miles-per-gallon (MPG) can be calculated with the following formula: MPG = Miles driven ÷ Gallons of gas used. Write a program that asks the user for the number of miles driven and the gallons of gas used. It should calculate the car's MPG and display the result.*

      print("Please enter the number miles that you have driven:")
      miles = int(input());
      print("Please enter the number of gallons of gas that you have used:")
      gallons = int(input());

      mpg = (miles / gallons);
      print(mpg, 'is your mpg');

    ```
    print("Please enter the number miles that you have driven:")
    miles = int(input());
    print("Please enter the number of gallons of gas that you have used:")
    gallons = int(input());

    mpg = (miles / gallons);
    print(mpg, 'is your mpg');
    ```

  __2.9__

    *Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows: F=(C*9/5)+32. The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit.*

      print("Please enter the temperature in Celsius")
      temp_c = int(input());

      temp_f = ((temp_c*9/5)+32);
      print(temp_f, 'is the converted temperature');

    ```
    print("Please enter the temperature in Celsius")
    temp_c = int(input());

    temp_f = ((temp_c*9/5)+32);
    print(temp_f, 'is the converted temperature');
    ```

  __2.11__

    *Write a program that asks the user for the number of males and the number of females registered in a class. The program should display the percentage of males and females in the class. Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage of females can be calculated as 12 ÷ 20 = 0.6, or 60%.*

      print("Please enter the number of males in your class:");
      male_num = int(input());
      print("Please enter the number of females in your class:");
      female_num = int(input());

      total_students = (male_num + female_num);
      male_percentage = ((male_num / total_students)*100);
      female_percentage = ((female_num / total_students)*100);

      print('The class population is ', male_percentage,'%', 'male and ', female_percentage,'%', 'female');

    ```
    print("Please enter the number of males in your class:");
    male_num = int(input());
    print("Please enter the number of females in your class:");
    female_num = int(input());

    total_students = (male_num + female_num);
    male_percentage = ((male_num / total_students)*100);
    female_percentage = ((female_num / total_students)*100);

    print('The class population is ', male_percentage,'%', 'male and ', female_percentage,'%', 'female');

    ```

  __Bonus Question__

    *Write a simple program with Turtle.  You may use the book’s examples.  The idea is to get some experience with Turtle.*

      import turtle

      star = turtle.Turtle()

      star.pencolor("blue")
      for i in range(5):
        star.forward(50)
        star.right(144)

      star.pencolor("red")
      for i in range(5):
        star.forward(50)
        star.left(144)

      turtle.done()
