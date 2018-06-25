s=0 
for x in range(1,1000): 
    c=0 
for y in range(1,x+1): 
    ds = x % y 
    if ds==0: 
        c=c+1 
    if c==2: 
        s=s+x 
print(s)