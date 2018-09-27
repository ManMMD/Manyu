n=eval(raw_input('Enter an integer,the input ends if it is 0:'))
s1=0
s2=0
i=0
j=0
while n!=0:
    if n>0:
        s1=s1+n
        i+=1
    else:
        s2=s2+n
        j+=1
    n=eval(raw_input('Enter an integer,the input ends if it is 0:'))
x=s1/(i*1.0)
y=s2/(j*1.0)
print('{}:{}\n{}:{}'.format(i,x,j,y))
