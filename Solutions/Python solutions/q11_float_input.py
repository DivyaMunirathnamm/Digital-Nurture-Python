def kg_to_lbs():
    kg = input("Enter weight in kg: ")
    try:
        kg = float(kg)
        lbs = kg * 2.20462
        print(f"Weight in pounds: {lbs:.2f}")
    except ValueError:
        print("Invalid input")
kg_to_lbs()