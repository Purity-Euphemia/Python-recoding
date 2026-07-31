numbers = [1, 2, 3]
try:
    print(numbers[3])
except IndexError as e:
    print("An error occurred:", e)