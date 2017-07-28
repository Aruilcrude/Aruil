lenx = open('E:/grep/crude/data.txt','r')
xue  = open('E:/grep/crude/1.txt','w')
leng = open('E:/grep/crude/2.txt','w')
lengxue = input("请输入性别:")
def feng(lengxue):
    if lengxue == '男':
        for link in lenx.readlines():
            fen = link.split()
            if fen[2] == '男':
                xin = str(fen + '\n')
                xue.writelines(xin)

    elif lengxue == '女':
        for link in lenx.readlines():
            fen = link.split()
            if fen[2] == '女':
                file = str(fen + '\n')
                leng.writelines(file)
leng.close()
xue.close()


