def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Invalid input")
        return

    return a + b

result = add(5, 3)
print("Sum:", result)