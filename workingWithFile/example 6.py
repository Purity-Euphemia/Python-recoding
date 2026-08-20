file = open("names.txt", "r")  # r means read
content = file.read()
print(content)
file.close()