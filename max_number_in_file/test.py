"""
Program to find the largest number in a text file
"""
import random;

with open("numbers.txt", "w") as f:
    for i in range(100_000):
        f.write(str(random.randint(1, 1_000_000_000)) + "\n")
    f.close()

max_number = 0
# find the largest number in the file (numbers.txt)
with open("numbers.txt", "r") as f:
    for line in f:
        max_number = max(max_number, int(line))

print(max_number)
    