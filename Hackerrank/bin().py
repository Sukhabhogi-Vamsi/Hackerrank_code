class myobject:
    def __init__(self ,x,y):
        self.x = x
        self.y = y

    def __index__(self):
        return self.x + self.y

obj = myobject(3,2)
print(bin(obj)[2:])