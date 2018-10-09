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
    
a,b,c,d,e,f=eval(raw_input('Enter a,b,c,d,e,f:'))
m=LinearEquation(a,b,c,d,e,f)
if m.isSolvable()!=True:
    print('The equation has on solution')
else:
    print('x is '+str(m.getX())+' and '+'y is '+str(m.getY()))

