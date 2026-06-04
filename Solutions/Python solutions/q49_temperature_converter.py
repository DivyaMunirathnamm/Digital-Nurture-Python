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