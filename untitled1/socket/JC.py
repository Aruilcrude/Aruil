#coding = utf-8
from time import ctime,sleep

def muisc():
    for lenx in range(2):
        print ("HELLO WROLD. %s" %ctime())
        sleep(1)

def move():
    for xue in range(2):
        print("HOW ARE YOU %s" %ctime())
        sleep(5)

if __name__=='__main__':
    muisc()
    move()
    print("该去睡觉了")