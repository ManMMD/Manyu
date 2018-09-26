x,y,z=eval(raw_input('Enter three edges:'))
if (x+y>=z) and (x+z>=y) and (y+z>=x):
    print('The perimeter is '+str(x+y+z))
else:
    print('No')
