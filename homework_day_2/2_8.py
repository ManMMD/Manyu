import random
def zhuan(n):
    if n==0:
        return 'scissor'
    elif n==1:
        return 'rock'
    else:
        return 'paper'
x=eval(raw_input('scissor(0),rock(1),paper(2):'))
c=random.randint(0,2)
if x==c:
    print('The computer is '+zhuan(c)+'.You are '+zhuan(x)+'.It is a draw')
elif x==0:
    if c==1:
         print('The computer is '+zhuan(c)+'.You are '+zhuan(x)+'.Computer won')
    elif c==2:
         print('The computer is '+zhuan(c)+'.You are '+zhuan(x)+'.You won')
elif x==1:
    if c==0:
         print('The computer is '+zhuan(c)+'.You are '+zhuan(x)+'.You won')
    elif c==2:
        print('The computer is '+zhuan(c)+'.You are '+zhuan(x)+'.Computer won')
elif x==2:
    if c==0:
        print('The computer is '+zhuan(c)+'.You are '+zhuan(x)+'.Computer won')
    elif c==1:
        print('The computer is '+zhuan(c)+'.You are '+zhuan(x)+'.You won')
