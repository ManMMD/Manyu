class Rectangle:
    def __init__(self,width=1,height=2):
        self.width=width
        self.height=height
        print('Width:'+str(self.width))
        print('Height:'+str(self.height))
    def getArea(self):
        print('Area:'+str(self.width*self.height))
    def getPerimeter(self):
        print('Perimeter:'+str(self.width*2+self.height*2))

m=Rectangle(4,40)
m.getArea()
m.getPerimeter()
n=Rectangle(3.5,35.7)
n.getArea()
n.getPerimeter()

