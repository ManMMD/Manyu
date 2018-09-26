def Today(n):
    if n==0:
        return 'Sunday'
    elif n==1:
        return 'Monday'
    elif n==2:
        return 'Tuesday'
    elif n==3:
        return 'Wednesday'
    elif n==4:
        return 'Thursday'
    elif n==5:
        return 'Friday'
    elif n==6:
        return 'Saturday'
x=eval(raw_input('Enter today is day:'))
y=eval(raw_input('Enter the number of days elapsed since today:'))
s=(x+y)%7
print('Today is '+Today(x)+' and the future day is '+Today(s))
