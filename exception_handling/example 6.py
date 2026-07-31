try:
    number = int(input("Enter a number:"))
    print(number)

except ValueError:
    print("That is not a valid whole number.")