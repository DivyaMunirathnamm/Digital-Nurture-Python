# Python Output Screenshots

This folder contains selected output screenshots from the Python programs completed as part of the Cognizant Digital Nurture 5.0 training program.

Due to the large number of exercises, only a representative set of screenshots has been included. These screenshots demonstrate the successful execution of programs covering various Python concepts such as:

* Functions
* Conditional Statements
* Loops
* File Handling
* Exception Handling
* Object-Oriented Programming
* Real-Time Applications

The screenshots are provided for demonstration and verification purposes and do not include outputs from every individual program.

## Sample Programs Included

### Q17 - Countdown Program

Demonstrates the use of while loops and control flow.
# CODE:
```
def countdown(count):
    if count <= 0:
        print("Invalid count")
        return

    while count > 0:
        print(count)
        count -= 1

countdown(5)
```
# OUTPUT:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f1d18d46-059d-485a-a0b6-fc20a042e42a" />

### Q37 - Multiple Instances

Demonstrates object-oriented programming concepts using classes and multiple objects.
# CODE:
```
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee Name:", self.name)

emp1 = Employee("John")
emp2 = Employee("David")

emp1.display()
emp2.display()
```

# OUTPUT:

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a78446fe-f40d-4969-8e78-ea0659fde162" />


### Q41 - Employee Management System

Demonstrates classes, dictionaries, JSON file handling, and data management.
# CODE:
```
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
```
# OUTPUT:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/552cb4dc-6bc2-411f-b624-a33bd87ca7dd" />


### Q44 - CSV Data Processor

Demonstrates CSV file processing, list comprehensions, filtering, and average salary calculation.

# CODE:
```
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
```
# OUTPUT:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/688bf7f0-da4f-4a80-91c1-ad868218135f" />


### Q47 - Calculator Program

Demonstrates functions, user input, arithmetic operations, and exception handling.
# CODE:
```
def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid Operator"

    except ZeroDivisionError:
        return "Cannot divide by zero"

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+,-,*,/): ")

    print("Result:", calculate(a, b, op))

except ValueError:
    print("Invalid Number")
```


# OUTPUT:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6f997a6c-1de8-4d61-8409-7c983197b3aa" />

### Q49 - Temperature Converter

Demonstrates class-based design, temperature conversions, user interaction, and formatted output.

# CODE:
```.c
from tabulate import tabulate

class Converter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

    def c_to_k(self, c):
        return c + 273.15

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def k_to_c(self, k):
        return k - 273.15

converter = Converter()

print("1. Celsius to Fahrenheit & Kelvin")
print("2. Fahrenheit to Celsius")
print("3. Kelvin to Celsius")

choice = int(input("Enter choice: "))

if choice == 1:
    c = float(input("Enter Celsius: "))

    data = [
        ["Celsius", f"{c:.2f}"],
        ["Fahrenheit", f"{converter.c_to_f(c):.2f}"],
        ["Kelvin", f"{converter.c_to_k(c):.2f}"]
    ]

elif choice == 2:
    f = float(input("Enter Fahrenheit: "))

    data = [
        ["Fahrenheit", f"{f:.2f}"],
        ["Celsius", f"{converter.f_to_c(f):.2f}"]
    ]

elif choice == 3:
    k = float(input("Enter Kelvin: "))

    data = [
        ["Kelvin", f"{k:.2f}"],
        ["Celsius", f"{converter.k_to_c(k):.2f}"]
    ]

else:
    print("Invalid Choice")
    exit()

print(tabulate(data, headers=["Type", "Value"], tablefmt="grid"))
```

# OUTPUT:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/27fbee5e-09e6-4d20-83ea-88df3ab66ec9" />

## Note

Only selected screenshots have been uploaded to maintain repository clarity and organization. The complete source code for all 55 Python exercises is available in the Python Solutions folder.

For complete implementations and additional exercises, please refer to the corresponding Python program files.
