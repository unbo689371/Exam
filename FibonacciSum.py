nterms = int(input("你需要幾項?"))

n1 = 0
n2 = 1
count = 2

if nterms <=0:
    print("請輸入一個正整數。")
elif nterms == 1:
    print("婓波那契數列:")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1,",",n2,end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth,end=" , ")

        n1 = n2
        n2 = nth
        count += 1


if nth%2 == 0 or n1%2==0 or n2%2 ==0:
    sum = 0
    sum = sum + nth
    print(sum)
else:
    print('奇數')
    

a1 = 1
a2 = 1
while a3<4000000:
    a3 +=1
for i in range(3, 101):
        a3 = a1 + a2
        print(a3)
        a1 = a2
        a2 = a3
        
