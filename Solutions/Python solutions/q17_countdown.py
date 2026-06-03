def countdown(count):
    if count <= 0:
        print("Invalid count")
        return

    while count > 0:
        print(count)
        count -= 1

countdown(5)