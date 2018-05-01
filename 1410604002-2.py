a1 = 1
a2 = 1
a3 =a1+a2
sum=0
while a3<4000000:
    if (a3%2)==0:
        sum=sum+a3
    a3 = a1 + a2
    a1 = a2
    a2 = a3
print(sum)
