def grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
        return
    if score >= 80:
        print("Grade A")
    elif score >= 60:
        print("Grade B")
    else:
        print("Grade C")
score = 88
grade(score)