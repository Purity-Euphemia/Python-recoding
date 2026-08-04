try:
    number = int("10")
    print(number)

except ValueError:
    print("Invalid number.")

else:
    print("Conversion was successful.")