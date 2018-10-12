import random
def shuffle(lst):
    l= len(lst)
    s=[]
    for i in range(l):
        n=random.randint(0,len(lst)-1)
        s.append(lst[n])
        lst.pop(n)
    print(s)

if __name__ == '__main__':
    a=raw_input('>>')
    b=a.split()
    print(b)
    shuffle(b)
