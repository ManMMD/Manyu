import math
x,y=raw_input('Enter the radius and length of a cylinder:').split()
radius=float(x)
length=float(y)
area=radius*radius*math.pi
volume=area*length
print('The area is '+str(area)+'\n'+'The volume is '+str(volume))
