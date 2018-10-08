import random
def sezi():
    x=random.randint(1,6)
    y=random.randint(1,6)
    s=x+y
    print('Yor rolled '+str(x)+'+'+str(y)+'='+str(s))
    return s
S=sezi()
if (S==2) or (S==3) or (S==12):
    print('You lose')
elif (S==7) or (S==11):
    print('You win')
else:
    n=S
    S=sezi()
    while (S!=7) and (S!=n):
        S=sezi()
    if S==7:
        print('You lose')
    else:
        print('You win')
