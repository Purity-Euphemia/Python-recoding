try:
    value = int(input("Please enter a number: "))
    result = 10 / value

except ValueError:
    print("You must enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed")

else:
    print("Result:", result)

finally:
    print("This block is always executed.")