import json

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} - {self.name} - {self.salary}"

employees = {
    "101": Employee("101", "John", 50000),
    "102": Employee("102", "David", 60000)
}

data = {}
for emp_id, emp in employees.items():
    data[emp_id] = {
        "name": emp.name,
        "salary": emp.salary
    }

with open("emps.json", "w") as file:
    json.dump(data, file)

with open("emps.json", "r") as file:
    loaded = json.load(file)

for emp_id, details in loaded.items():
    print(emp_id, details["name"], details["salary"])