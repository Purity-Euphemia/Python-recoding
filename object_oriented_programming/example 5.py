class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def study(self):
        print(self.name, "is studying")


student1 = Student("John", "Python")

print(student1.name)
print(student1.course)

student1.study()