## MATH QUIZ

import random

variable_1 = random.randint(1,1000)
variable_2 = random.randint(1,1000)

solution = variable_1 + variable_2

print("What is the answer to this question: ", variable_1, "+", variable_2)
user_input = int(input("-->"))

if user_input == solution:
    print("CORRECT!!! good job")
else:
    print("NOPE!!! sorry wrong answer. The correct answer was: ", solution)
