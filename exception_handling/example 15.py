try:
    num = int(input("Enter a number: "))
    print(20 / num)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")