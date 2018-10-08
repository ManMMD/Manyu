def sumDigits(n):
    s=0
    while n!=0:
       s=s+n%10
       n=n/10
    return s

x=eval(raw_input('>>'))
print(sumDigits(x))
