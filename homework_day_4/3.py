import math
def displaySortedNumbers(num1,num2,num3):
    n=max(num1,num2,num3)
    m= min(num1,num2,num3)
    if num1!=n and num1!=m:
        return m,num1,n

    elif num2!=n and num2!=m:
        return m,num2,n

    else:
        return m,num3,n

x,y,z=eval(raw_input('Enter three numbers:'))
print('THE sorted numbers are {}'.format(displaySortedNumbers(x,y,z)))


