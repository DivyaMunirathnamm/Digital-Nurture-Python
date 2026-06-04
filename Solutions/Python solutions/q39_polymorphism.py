class Employee:
    def work(self):
        print("Employee working")

class Developer(Employee):
    def work(self):
        print("Developer writing code")

class Manager(Employee):
    def work(self):
        print("Manager managing team")

employees = [Developer(), Manager()]

for emp in employees:
    emp.work()