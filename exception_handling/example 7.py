try:
    answer = 10 / 0
    print(answer)

except ZeroDivisionError:
    print("You cannot divide by zero.")