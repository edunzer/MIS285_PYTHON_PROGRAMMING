print("Please enter the total square feet you want to convert into acres");
square_ft_input = int(input());
x = 43560;

acre_output = (square_ft_input / x);
print(square_ft_input, 'is ', acre_output, 'acres');
