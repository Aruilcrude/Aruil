lenx = open("E:/grep/xue/pren.txt","w")
xue  = open("E:/grep/gl/lx.txt","r")

fin  = set(xue)
for li in fin:
    lenx.write(li)
lenx.close()


