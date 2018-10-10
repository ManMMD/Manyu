def countLetters(s):
    n=0
    for i in s:
        if i >='A' and i <='z':
            n+=1
    print('zimu:'+str(n))


S=raw_input('>>')
countLetters(S)
