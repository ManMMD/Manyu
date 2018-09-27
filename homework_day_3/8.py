s=0
k=1
f=0
i=1
while i<=100000:
    q=1/(i*1.0)
    s=s+k*q
    k=k*-1
    i=i+2
    f=f+1
    if f==5000:
        print('i='+str(i-1)+'\tp='+str(4*s))
        f=0

