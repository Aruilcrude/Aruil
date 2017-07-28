#coding = utf-8
def lenx(s):
    if s.strip() is "":   #判断s 是否等于空
        return 8   #为真输出返回值
    elif s < 0 :   #判断s 是否为一个负数
        return -1  #为真返回输出值
    elif int(s):   #判断s 是否是一个int 整数
        return 15
print(lenx(""))     #对lenx 进行赋值