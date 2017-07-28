lenx = list()
xue  = open("E:/grep/xue/xue.txt","w")
xin  = open("E:/grep/gl/ls.txt","r")
for fen in xin:
    fenx = list(fen)
    if fenx[1] not in lenx:
        xue.write(fen)
        print(fen)
xue.close()
