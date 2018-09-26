import math
x1,y1=eval(raw_input('Enter point 1:'))
x2,y2=eval(raw_input('Enter point 2:'))
radius=6371.01
d=radius*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y1-y2)))
print('The distance between the two poi1ts is '+str(d) +'km')
