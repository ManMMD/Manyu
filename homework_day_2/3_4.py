import math
n=eval(raw_input('Enter the number of sides:'))
s=eval(raw_input('Enter the side:'))
area=n*s*s/(4*math.tan(math.pi/n))
print('The area of the polygon is '+str(area))
