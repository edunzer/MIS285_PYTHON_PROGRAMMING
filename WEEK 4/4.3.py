## BUDGET ANALYSIS
x = 0
budget = 0

budget = input("Please enter your budget:")
budget = int(budget)
num = int(input("Please enter money spent (enter 0 to quit): "))

while num != 0:
  x = x + num
  num = int(input("Please enter money spent (enter 0 to quit): "))

if x > budget :
  end = x - budget
  print("You went over your budget by: ", end)

elif x < budget:
  end = budget - x
  print ("You are under budget by: ", end)
