from math import factorial

number = factorial(100)
sum = 0
for digit in str(number):
    sum = sum + int(digit)
print(sum) 



a1 = 1
a2 = 1
a3 = a1 + a2
while a3<4000000:
    if a3%2==0:
        
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        
