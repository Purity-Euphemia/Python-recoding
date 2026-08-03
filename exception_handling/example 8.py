try:
    number = int(input("Enter a number:"))
    answer = 10 / number
    print(answer)   

except ValueError:
    print("Please enter a valid whole number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")