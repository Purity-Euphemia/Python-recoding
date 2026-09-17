class Employee:

    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def work(self):
        print(self.name, "is working")


employee1 = Employee("Purity", "Software Engineer", 300000)

print(employee1.name)
print(employee1.job)
print(employee1.salary)

employee1.work()