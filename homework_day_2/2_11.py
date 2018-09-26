s=raw_input('Enter a three-digit integer:')
n=s[::-1]
if s==n:
    print(s+' is a palindrome')
else:
    print(s+' is not a palindrome')
