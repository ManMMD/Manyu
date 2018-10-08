import math
def printChars(ch1,ch2,numberPerLine):
    for i in range(1,ord(ch2)-ord(ch1)):
        print('{} '.format(chr(ord(ch1)+i)),end='')
        if i%numberPerLine==0:
            print()
s1='1'
s2='Z'
n=10
printChars(s1,s2,n)
