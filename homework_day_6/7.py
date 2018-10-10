def guize_1(n):
    if len(n)>=13 and len(n)<=16:
        if n.startswith('4')==True or n.startswith('5')==True or n.startswith('37')==True or n.startswith('6')==True:
            return True

def suanfa_1(n):
    sum_=0
    for i in n:
        z=int(i)*2
        if z>=10:
            a=z%10
            b=z/10
            z=a+b
        sum_=sum_+z
    return sum_

def suanfa_2(n):
    sum_=0
    for i in range(1,len(n)):
        if i%2!=0:
            sum_+=int(n[i])
    return sum_

def isValid(S):
    if guize_1(S)==True:
        if (suanfa_1(S)+suanfa_2(S))%10==0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

a=raw_input('Enter number:')
isValid(a)


