## PRIME NUMBER GENERATION

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
