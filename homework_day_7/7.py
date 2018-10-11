import random
def shuffle(lst):
    l= len(lst)
    s=[]
    for i in range(len(lst)):
        n=random.randint(0,l-1)
        s.append(lst[n])
        lst.pop(n)
        l -= 1
    print(s)

if __name__ == '__main__':
    a=raw_input('>>')
    b=a.split()
    print(b)
    shuffle(b)
