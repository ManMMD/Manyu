x,y=eval(raw_input('year,month:'))
if (y==1) or (y==3) or (y==5) or (y==7) or (y==8) or (y==10) or  (y==12) :
    print('31')
elif (y==2):
    if (x%4==0) and (x%100!=0) or (x%400==0):
        print('29')
    else:
        print('28')
else:
    print('30')
