def sum_odd_numbers():
    total = 0

    for i in range(10):
        if i % 2 == 0:
            continue

        total += i

    print("Sum of odd numbers:", total)

sum_odd_numbers()