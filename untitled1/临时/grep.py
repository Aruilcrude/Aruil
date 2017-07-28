lenx = set()
fen  = open("E:/grep/LX/fen.txt","w")
xue  = open("E:/grep/LX/xue.txt","r")
while True:
    feng = xue.readline()
    if feng:
        feng+=1
        fen.write(feng)

fen.close()

