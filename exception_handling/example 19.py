try:
    num = int(input("Enter a number: "))
    number = int(input("Enter a second number: "))
    print(num / number)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("You cannot divide by zero.")