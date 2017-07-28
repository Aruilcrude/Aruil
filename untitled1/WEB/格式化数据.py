xue  = open("E:/grep/xue/xue.txt","w")
lenx = open("E:/grep/xue/lenx.txt","r")
def f1():
    with open("1.txt", "r") as f:
        for s in f:
            l = s.rsplit()
            t = '{0:-<25} {1: >7} {2}'.format(l[0], l[1], l[2])
            print(str(t))

fenx = (f1(lenx))
xue.write(fenx)
xue.close()