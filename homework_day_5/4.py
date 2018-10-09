class Fan:
    SLOW=1
    MEDIUM=2
    FAST=3
    def __init__(self,speed=SLOW,radius=5,color='blue',on=False):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__color=color
        print('Speed:'+str(self.__speed))
        print('Radius:'+str(self.__radius))
        print('Color:'+str(self.__color))
        print('On:'+str(self.__on))

print('--------1--------')
Fan(Fan.FAST,10,'yellow',True)
print('--------2--------')
Fan(Fan.MEDIUM)



