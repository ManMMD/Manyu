import random
flower=['Spades','Clubs','Hearts','Diamonds']
size=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
flag = 0
n=0
pass_=[]
while flag!=4:
    x=random.randint(0,3)
    y=random.randint(0,12)
    if flower[x] not in pass_:
        pass_.append(flower[x])
        print(flower[x]+' of '+size[y])
        flag += 1
    n += 1
print('Number of picks:'+str(n))
