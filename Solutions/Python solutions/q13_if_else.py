def even_odd(num):
    if not isinstance(num, int):
        print("Invalid input")
        return
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
num = 8
even_odd(num)