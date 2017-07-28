class lenx():
    def __init__(self,name):
        self.name = name

class xue(lenx):
    def __init__(self,name,email):
        super().__init__(name)
        self.email = email

fen = xue('lengxue','aruilture@163.com')
print(fen.name)
print(fen.email)
