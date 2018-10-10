def suanfa(s):
    sum_=0
    for i in range(0,len(s)):
        if i%2==0:
            sum_+=int(s[i])
        else:
            sum_+=3*int(s[i])
    d=10-sum_%10
    if d==10:
        d=0
    return d

S=raw_input('Enter the firsy 12 digits of an ISBN-13 as a string:')
print('The ISBN-13 number is '+S+str(suanfa(S)))
