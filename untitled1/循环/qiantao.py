lenx = range(2,8)
xue  = range(2,8)
for xin in lenx:
    for fen in xue:
        print(xin,fen)

lenx = range (6,21)
xue  = range (8,20)
lengxue = [(xin,fen) for xin in lenx for fen in xue ]
for fengxin in lengxue :
    print (fengxin)
for xin,fen in lengxue:
    print(xin,fen)