num=eval(raw_input('Enter a number between 0 and 1000:'))
s=0
while(num!=0):
   s=num%10+s
   num=num/10
print('The sum of the digits is '+str(s))
