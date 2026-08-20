with open('example.txt', 'w') as file:
    file.write("Hello, python!\n")
    file.write("Writing to files is essential.")

with open('example.txt', 'r') as file:
    file.write("\nAppending a new line to the file.")  # This will raise an error because the file is opened in read mode