s1=0
s2=0
n=1
m=50000
while n<50001:
    s1=s1+1/(n*1.0)
    n+=1
while m>0:
    s2=s2+1/(m*1.0)
    m=m-1
print('s1='+str(s1))
print('s2='+str(s2))
