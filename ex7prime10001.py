import math
def prime(n):
    m=int(math.sqrt(n))+1
    for i in range(2,m):
        if n%i==0:
            return False
    return True
count=0
i=2
while count<10001:
    if prime(i):
        count=count+1
    if count!=10001:
        i=i+1
print(i)

#ANS=104743
