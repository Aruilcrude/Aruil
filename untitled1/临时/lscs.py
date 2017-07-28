lenx = set()
fen  = open ("E:/grep/xue/lenx.txt","w")
xue  = open("E:/grep/gl/lx.txt","r")

for lx in xue:
        xin = lx.split()
        fenx = xin[1]
        if fenx not in lx:
            fen.write(fenx)
            lenx.add(lx)
fen.close()
