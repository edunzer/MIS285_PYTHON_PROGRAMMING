## MONTHLY SALES TAX

sales_input = int(input("Please enter in the total amount of sales income for this month -->"))

state_tax = float(0.05)
county_tax = float(0.025)

state_total = sales_input * state_tax
county_total = sales_input * county_tax
total_tax = state_total + county_total

print("Here is your calculated state tax: ",state_total)
print("Here is your calculated county tax: ",county_total)
print("Here is your total calculated tax: ", total_tax)
