import math
def futureInverstmentValue(m,l,y):
    m=m*((1+l/12)**12)
    print(str(y)+'\t'+str(round(m,2)))
    return m

money=raw_input('The amount invested:')
li=raw_input('Annual interest rate:')

num_money=int(money)
num_li=int(li)
num_li=num_li*0.01

print('Years\tFuture Value')

for i in range(1,31):
    num_money=futureInverstmentValue(num_money,num_li,i)
