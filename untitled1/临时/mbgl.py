fen  = open ("E:/grep/xue/G4/6.txt","w")
xue  = open("F:/G4-2/6.txt","r")

for lx in xue:
        xin = lx.split()
        fenx = xin[1]
        fen.write(fenx+'\n')
fen.close()
