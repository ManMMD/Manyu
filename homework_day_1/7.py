money=eval(raw_input('Enter the monthly saving amount:'))
i=1
s=0
while(i<=6):
    s=(money+s)*(1+0.00417)
    i=i+1
print('After the sixth month,the account value is '+str(s))
