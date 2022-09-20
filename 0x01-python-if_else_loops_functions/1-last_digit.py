#!/usr/bin/python3
import random
number = random.randint(-10, 100)
num2 = number % 10
if num2 > 5:

    print(f"the last digit of, {number} is, {num2} and is greater than 5")
elif num2 < 6 and num2 != 0:
    print(f"the last digit of, {number} is, {num2} and is less than 6 and is not 0")
else:
    print(f"the last digit of, {number} is, {num2}  and is 0")
