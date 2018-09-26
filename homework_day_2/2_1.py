import math
a,b,c=eval(raw_input('Enter a b c:'))
s=b*b-4*a*c
if s>0:
    print('The roots are '+str((-1*b+math.sqrt(s))/(2*a))+' and '+str((-1*b-math.sqrt(s)/(2*a))))
elif s==0:
    print('The root is '+str((-1*b+math.sqrt(s))/(2*a)))
else:
    print('The equation has no real roots')
