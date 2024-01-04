"""
HW2
Savchenko Kirill
"""
from statistics import mean

number = int(input("enter 3-digit number: "))

number_1 = number // 100 % 10
number_2 = number // 10 % 10
number_3 = number % 10
num_list = [number_1, number_2, number_3]

operation = input("what do you want to do? (min, max, mean): ")

if operation == "max":
    print(max(number_1, number_2, number_3))
elif operation == "min":
    print(min(number_1, number_2, number_3))
elif operation == "mean":
    print(mean(num_list))
else:
    print("Error")