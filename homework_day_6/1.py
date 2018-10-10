def jiance(a):
    n=0
    for i in a:
        if i>='0' and i<='9':
            n+=1
    
    if len(a)==11 and n==9: 
        if a[3]=='-' and a[6]=='-':
            a=a.replace('-','0')
            if a.isalnum()==True:
                print('Valid SSN')
    else:
        print('Invalid SSN')


s=raw_input('play str ddd-dd-dddd:')
jiance(s)
