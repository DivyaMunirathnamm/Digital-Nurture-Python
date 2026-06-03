def split_bill(total_bill, people):
    if total_bill <= 0 or people <= 0:
        print("Invalid input")
        return
    share = total_bill // people
    print(f"Individual Share: {share}")
total_bill = 1250
people = 4
split_bill(total_bill, people)