for i in range (1,10000):
    s=0
    for k in range(1,i):
        if i%k==0:
            s=s+k
    if i==s:
        print(i)
