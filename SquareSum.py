sum = 0
t = 0

for i in range(1, 101):
        sum = sum + i ** 2
print(sum)

for i in range(1, 101):
        t = t + i
print(t**2)

print(t**2 - sum)