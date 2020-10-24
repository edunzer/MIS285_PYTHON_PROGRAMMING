## AUTOMOBILE COSTS

print("Please enter in the amounts for the following monthly costs of your vehicle:")

loan_input = int(input("loan -->"))
insurance_input = int(input("insurance -->"))
gas_input = int(input("gas -->"))
oil_input = int(input("oil -->"))
tires_input = int(input("tires -->"))
maintence_input = int(input("maintence -->"))

monthly_total = loan_input + insurance_input + gas_input + oil_input + tires_input + maintence_input
print("Here is your monthly total: ",monthly_total)
annual_total = monthly_total * 12
print("Here is your annual total: ",annual_total)
