lenx = open("E:/grep/LX/xue.txt","r")
i = 0
for i in range(1000000):
    i += 1
    readstring = lenx.readline().strip('\n')
    stringlen =('-%s' % (str(i)))
    lenx = '%s-$s\n' %s(readstring,stringlen)
    with open('E:/grep/xue/fen.txt', 'a') as xyz:
        xyz.write(stringlen)

    print (stringlen)