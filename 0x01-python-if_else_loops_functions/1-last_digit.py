#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
elif number < 0:
    last_digit = -(-number % 10)
elif number == 0:
    last_digit = 0

str = "Last digit of {} is {}".format(number, last_digit)
if last_digit > 5:
    print(f"{str} and is greater than 5")
elif last_digit == 0:
    print(f"{str} and is 0")
elif 6 > last_digit != 0:
    print(f"{str} and is less than 6 and not 0")
