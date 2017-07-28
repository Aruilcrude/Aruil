lines_seen = set()      #创建个空的集合
outfile = open("out.txt", "w")   #创建个空的文档

for line in open("1.txt", "r"):      #以读取每行来打开文档
    lines_seen.add(line)             #把文档数据传入集合
for line in open("2.txt", "r"):      #打开第二个文档
    lines_seen.add(line)             #把第二个文档导入集合
if line not in lines_seen:#判断集合
    outfile.write(line)              #写入集合
outfile.close()                      #关闭文档