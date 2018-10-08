import math
def getPentagonalNumber(n):
    return n*(3*n-1)/2

k=0
for i in range(1,101):
    print('{} '.format(round(getPentagonalNumber(i))),end='')
    k+=1
    if k==10:
        print()
        k=0
