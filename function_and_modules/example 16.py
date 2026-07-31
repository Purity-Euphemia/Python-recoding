def number_type(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = number_type(7)
print("The number is:", result)