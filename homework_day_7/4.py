def pinjun(n):
    sum_=0
    l=len(n)
    for i in n:
        sum_ += int(i)
    return sum_/(l*1.0)

def bijiao(n):
    big=0
    small=0
    for i in n:
        if int(i)>=pinjun(n):
            big += 1
        else:
            small +=1
    print('Big:'+str(big))
    print('Small:'+str(small))

if __name__ == '__main__':
    a = raw_input('Enter sorce:')
    s=a.split()
    bijiao(s)
