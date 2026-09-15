class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(self.name,"is studying")

Student1 = Student("John", 20)
print(Student1.name)