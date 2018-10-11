a=raw_input('Enter integers between 1 and 100:')
l=a.split()
print(l)
for i in range(101):
    if l.count(str(i))!=0:
        if l.count(str(i))==1:
            print(str(i)+' occurs '+str(l.count(str(i)))+' time')
        else:
           print(str(i)+' occurs '+str(l.count(str(i)))+' times')


