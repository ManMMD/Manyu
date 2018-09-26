import random
x=random.randint(1,100)
y=random.randint(1,100)
print(str(x)+'+'+str(y)+'=?')
n=eval(raw_input('>>'))
if n==(x+y):
    print('True')
else:
    print('False')
