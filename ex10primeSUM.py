primes = [2]
n = 3
sum = 5
while n < 2000000 :
        max = n ** 0.5
        for i in primes:
                if n % i == 0:
                        break
                if i > max:
                        primes.append(n)
                        break
        n = n + 2
        sum = sum + i
print(sum)