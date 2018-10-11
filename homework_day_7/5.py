import random
a=[0,0,0,0,0,0,0,0,0,0]
for i in range(1001):
    a[random.randint(0,9)] += 1
print(a)
