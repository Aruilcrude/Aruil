lines_seen = set()     #创建一个空集合
outfile = open("E:/grep/xue/xuex.txt","w")     #打开一个文件  用写入的方式
for line in open("E:/grep/gl/lx.txt","r"):  #循环读取一个文件
    if line not in lines_seen:  #判断
        outfile.write(line)     #写入文件
        lines_seen.add(line)    #把lines_seen写入创建的集合当中
outfile.close()                 #然后关闭文件