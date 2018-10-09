import math

class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    
    def isSolvable(self):
        if (self.__a*self.__d-self.__b*self.__c)!=0:
            return True

    def getX(self):
        x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        return x
    
    def getY(self):
        y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        return y

x1,y1,x2,y2=eval(raw_input('Enter the endpoints of the first line segment:'))
x3,y3,x4,y4=eval(raw_input('Enter the endpoints of the second line segment:'))
a=y1-y2
b=x2-x1
e=x2*y1-x1*y2
c=y3-y4
d=x4-x3
f=x4*y3-x3*y4
print(a,b,e,c,d,f)
m=LinearEquation(a,b,c,d,e,f)
if m.isSolvable()!=True:
    print('The equation has on solution')
else:
    print('The intersecting point is:('+str(m.getX())+','+str(m.getY())+')')



