lenx = ["hello wrold","How are you ", "lengxue "]

for xue in lenx :             #用for 来表明xue 在lenx 里面
    if xue == "lengxue ":      #判断xue 里面有没有"lengxue"
        print ("你好吗?")       #为真输出
        break                 #跳出循环
    print ("循环" + xue)       #再次执行一次xue 直到执行到"lengxue" 就停止

else:
    print ("没有完成数据循环!")    #为假 输出

print("完成循环 OK ")           #循环完成输出