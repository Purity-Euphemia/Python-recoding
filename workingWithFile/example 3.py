
import csv

# Writing to a CSV file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])
    writer.writerow(["Bob", 25])

# Reading from a CSV file
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for ro in reader:
        print(row)