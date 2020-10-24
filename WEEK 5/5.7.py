## STADIUM SEATING

class_a = 20
class_b = 15
class_c = 10

print("Please enter in the number of tickets sold for each class:")
a_input = int(input("Class A tickets -->"))
b_input = int(input("Class B tickets -->"))
c_input = int(input("Class C tickets -->"))

sold_a = a_input * class_a
sold_b = b_input * class_b
sold_c = c_input * class_c

print("Here is the total for Class A tickets: ", sold_a)
print("Here is the total for Class B tickets: ", sold_b)
print("Here is the total for Class C tickets: ", sold_c)
