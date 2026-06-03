def first_even(start, end):
    if start > end:
        print("Invalid range")
        return

    for i in range(start, end + 1):
        if i % 2 == 0:
            print("First even number:", i)
            break

first_even(1, 10)