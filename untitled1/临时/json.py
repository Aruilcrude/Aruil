lenx = open("E:/grep/LX/1.txt","r")
xue  = open("E:/grep/LX/fenx.txt","w")
for i in range(1,5002):
    lens =lenx.readline(17).strip('\n')
    fen  = ('-%s' % (str(i)))
    min  = (lens + fen)
    xue.writelines(min)
xue.close()


