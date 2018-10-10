def getNumber(uppercaseLetter):
    uppercaseLetter=uppercaseLetter.lower()
    if uppercaseLetter>='a' and uppercaseLetter<='c':
        return '2'
    elif uppercaseLetter>='d' and uppercaseLetter<='f':
        return '3'
    elif uppercaseLetter>='g' and uppercaseLetter<='i':
        return '4'
    elif uppercaseLetter>='j' and uppercaseLetter<='l':
        return '5'
    elif uppercaseLetter>='m' and uppercaseLetter<='o':
        return '6'
    elif uppercaseLetter>='p' and uppercaseLetter<='s':
        return '7'
    elif uppercaseLetter>='t' and uppercaseLetter<='v':
        return '8'
    elif uppercaseLetter>='w' and uppercaseLetter<='z':
        return '9'
    else:
        return uppercaseLetter

s=raw_input('Enter a string:')
S=''
for i in s:
    S=S+getNumber(i)

print(S)

