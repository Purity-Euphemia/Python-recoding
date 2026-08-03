try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input. Please enter a valid number.")

finally:
    print("The program has finished.")