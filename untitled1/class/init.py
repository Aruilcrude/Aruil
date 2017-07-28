class FEN():
    def __init__(self,name):
        self.name = name

    def xue(self):
        print("hello %s wrold" % self.name)

leng = FEN('李超')
leng.xue()