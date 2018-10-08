import math

def sushu(n):
    for i in range (2,int(math.sqrt(n))):
        if n%i==0:
            return 0
            break
    else:
        return 1

print('p\t2^p-1')
for j in range (2,32):
    if sushu(j)==1:
        if sushu (2**j-1)==1:
            print(str(j)+'\t'+str(2**j-1))
            j+=1
    else:
        j+=1


