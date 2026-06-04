import matplotlib.pyplot as plt

class Category:

    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

food = Category("Food", 5000)
travel = Category("Travel", 3000)

food.spent = 5500
travel.spent = 2000

for category in [food, travel]:
    if category.spent > category.limit:
        print(category.name, "Budget Exceeded")

plt.pie(
    [food.spent, travel.spent],
    labels=["Food", "Travel"]
)

plt.show()