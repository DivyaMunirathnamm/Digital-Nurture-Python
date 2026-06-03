def calculate_net_salary(salary, tax_rate):
    if salary < 0:
        print("Invalid salary")
        return

    if not (0 <= tax_rate <= 1):
        print("Invalid tax rate")
        return

    net_salary = salary - (salary * tax_rate)
    print(f"Net Salary: {net_salary:.2f}")

salary = 75000.5
tax_rate = 0.18

calculate_net_salary(salary, tax_rate)