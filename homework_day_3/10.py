k=0
for i in range(1,8):
    for j in range(i+1,8):
        k+=1
        print(str(i)+' '+str(j))
print('The total number of all combinations is '+str(k))
