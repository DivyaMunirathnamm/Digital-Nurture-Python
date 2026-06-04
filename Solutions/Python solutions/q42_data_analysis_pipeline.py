import statistics

try:
    with open("sales.txt", "r") as file:
        data = [float(line.strip()) for line in file]

    print("Mean:", statistics.mean(data))
    print("Median:", statistics.median(data))

except FileNotFoundError:
    print("File not found")

except ValueError:
    print("Invalid data")
    