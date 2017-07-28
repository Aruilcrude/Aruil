#如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
#例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。
for i in range(100,999):
    sum=0 #各个位数的立方和
    temp=i
    while temp:
        sum=sum+(temp%10)**3   #累加
        temp//=10   #地板除
    if sum==i:
        print(i)
