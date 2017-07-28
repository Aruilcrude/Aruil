
pattern = r'.*ActivityManager: Displayed (.*)/\.(.*): \+(.*)ms'
cs = open('./csv.txt', 'w')
csvw = csv.writer(cs)

f = open('D:/cs/xu.txt')
for line in f:
    m = re.match(pattern, line)
    if (m is not None):
        csvw.writerow(m.group(1, 2, 3))
f.close()
cs.close()