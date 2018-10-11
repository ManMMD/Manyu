def indexOfSmallestElement(lst):
    m=min(l)
    print(m)
    for i in range(len(l)):
        if l[i]==m:
            print(str(i)+' ',end="")
    print()



if __name__ == '__main__':
    
    a=input('>>')
    l=a.split()
    indexOfSmallestElement(l)
