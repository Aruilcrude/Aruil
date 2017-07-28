lines_seen = set()
outfile = open("E:/grep/xue/xin.txt", "w")

for line in open("E:/grep/gl/all-1.txt", "r"):
    lines_seen.add(line)
for line in open("E:/grep/gl/ASIN.txt", "r"):
    lines_seen.add(line)

for line in lines_seen:
    outfile.write(line)
outfile.close()