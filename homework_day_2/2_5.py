import math
x1,y1=eval(raw_input('Enter weight an price for package 1:'))
x2,y2=eval(raw_input('Enter weight an price for package 2:'))
if (x1/y1)>(x2/y2):
    print('Package 1 has the better price')
elif (x1/y1)<(x2/y2):
    print('Package 2 has the better price')

