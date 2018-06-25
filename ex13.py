# -*- coding: UTF-8 -*- 
numbers = [] 
count_num=0 
# 打開檔案 
file = open('D:/python/n.txt', 'r') 
# 讀取檔案 
for line in file.readlines():    #依序讀取每行 
    line = line.strip()    #去掉每行頭尾空白 
    numbers.append(int(line)) 
for x in range(0,len(numbers)): 
    asdf=int(int(numbers[x])/10000000000000000000000000000000000000000) 
    count_num=count_num+int(asdf) 
# 關閉檔案 
print(count_num) 
file.close()