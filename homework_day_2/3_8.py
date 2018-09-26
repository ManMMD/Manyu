file_handle=open('test.txt',mode='w')
s=raw_input('>>')
n=''
for i in s:
    n=n+chr((ord(i)+5))
file_handle.write(n)
file_handle.close()
