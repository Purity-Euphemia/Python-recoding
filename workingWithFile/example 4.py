import json

data = {
    "name": "John",
    "age": 28,
    "city": "New York"
}

# Writing JSON to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Reading JSON from a file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)