k=0
for i in range (100,1000):
    if (i%5==0) and (i%6==0):
        print('{} '.format(i),end=' ')
        k+=1
    if k==10:
        print()
        k=0

