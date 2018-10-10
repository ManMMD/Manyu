def jiance(s):
    n=0
    for i in s:
        if i>='0' and i<='9':
            n+=1        
    if (len(s)>=8) and (s.isalnum()==True) and (n>=2):
        print('valid password')
    else:
        print('invalid password')

S=raw_input('>>')
jiance(S)
