import re

# Open and read the file
filename = "regex_sum_2148311.txt"

with open(filename, "r") as file:
    data = file.read()

# Find all numbers using regex
numbers = re.findall(r"[0-9]+", data)

# Convert numbers to integers and sum them
total_sum = sum(map(int, numbers))

# Print the sum
print("Sum of numbers:", total_sum)
