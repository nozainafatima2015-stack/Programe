class rectangle():
    def __init__(self , l , w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width

newrectangle = rectangle(12 ,10)
print("Dimension of Rectangle - Length : %d Width : %d" % (newrectangle.length, newrectangle.width)) 
print("area of rectangle :" , newrectangle. rectangle_area())