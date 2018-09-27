import math
x=eval(raw_input('Loan Amount:'))
y=eval(raw_input('Number of Years:'))
n=0.05
print('Interest Monthly Payment Total Payment')
while n<0.08125:
    print(str(n*100)+'%\t\t'+str(round((x*math.pow(1+n,y))/(12*y),2))+'\t\t'+str(round(x*math.pow(1+n,y),2)))
    n+=0.00125
