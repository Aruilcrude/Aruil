class wrold():
    def __init__(self,text):
        self.text = text

    def lenx(self,FEN):
        return self.text.lower() == FEN.text.lower()

fish = wrold('lenx')
doy  = wrold('LENA')
hows = wrold('FENG')

print(fish.lenx(doy))