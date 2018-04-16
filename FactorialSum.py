from math import factorial

number = factorial(100)
sum = 0
for digit in str(number):
    sum = sum + int(digit)
print(sum)