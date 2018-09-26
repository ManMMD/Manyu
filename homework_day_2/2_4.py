import math
x,y,z=eval(raw_input('x,y,z:'))
Max=max(x,y,z)
Min=min(x,y,z)
if (x!=Max) and (x!=Min):
    k=x
elif (y!=Max) and (y!=Min):
    k=y
elif (z!=Max) and (z!=Min):
    k=z
print(str(Min)+' '+str(k)+' '+str(Max))
