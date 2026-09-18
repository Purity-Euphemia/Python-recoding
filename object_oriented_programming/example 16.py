class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(self.name, "is teaching", self.subject)

teacher1 = Teacher("Mrs Grace", "Python")

print(teacher1.name)
print(teacher1.subject)
teacher1.teach()