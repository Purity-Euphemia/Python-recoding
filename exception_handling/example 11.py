try: 
    first_number = float(input("Enter the first number:"))
    second_number = float(input("Enter the second number:"))
    answer = first_number / second_number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("The answer is:", answer)

finally:
    print("Calculation finished.")