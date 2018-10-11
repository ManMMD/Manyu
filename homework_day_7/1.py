def panduan(x,best):
    n=int(x)
    if n>=best-10:
        return 'A'
    elif n>=best-20:
        return 'B'
    elif n>=best-30:
        return 'C'
    elif n>=best-40:
        return 'D'
    else:
        return 'F'

a=raw_input('Enter scores:')
l=a.split(' ')
for i in range(len(l)):
    l[i]=int(l[i])
m=int(max(l))
print m
for i in range(len(l)):
    print('Student '+str(i)+' score is '+str(l[i])+' and grade is '+str(panduan(l[i],m)))
    



