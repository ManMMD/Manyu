n=10000
i=0
s=0
while i<13:
    n=n*(1+0.05)
    if i==9:
        print('ten year late:'+str(n))
    if i>=9:
        s=s+n
    i+=1
print(s)
