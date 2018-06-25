import datetime
sum = 0 
for y in range(1901,2001,1):
    for m in range(1, 13, 1):
        day = datetime.datetime(y, m, 1)
        if day.weekday() == 6:
            sum = sum + 1
print(sum)

#ANS=171
