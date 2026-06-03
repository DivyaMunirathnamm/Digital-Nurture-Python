def salary_stats(salaries):
    if not salaries:
        print("Salary list is empty")
        return
    print("Highest Salary:", max(salaries))
    print("Lowest Salary:", min(salaries))
salaries = [50000, 75000, 62000, 95000]
salary_stats(salaries)