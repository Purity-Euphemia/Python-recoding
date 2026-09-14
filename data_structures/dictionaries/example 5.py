# Using the get method to avoid KeyError
person = {"name": "Alice",
    "age": 30,
    "city": "New York"}

print("Age:", person.get("age", "Not available"))