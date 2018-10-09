import math

class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__s=side
        self.__x=x
        self.__y=y

    def getPerimeter(self):
        p=self.__n*self.__s
        print('Perimeter:'+str(p))

    def getArea(self):
        a=(self.__n*self.__s**2)/(4*math.tan(math.pi/self.__n))
        print('Area:'+str(a))

print('--------1--------')
RegularPolygon().getPerimeter()
RegularPolygon().getArea()
print('--------2--------')
RegularPolygon(6,4).getPerimeter()
RegularPolygon(6,4).getArea()
print('--------3--------')
RegularPolygon(10,4,5.6,7.8).getPerimeter()
RegularPolygon(10,4,5.6,7.8).getArea()


