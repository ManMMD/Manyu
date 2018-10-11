def isSorted(lst):
    flag=0
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        print('The list is not sorted')
    else:
        print('The list is already sorted')

if __name__ == '__main__':
    a = raw_input('Enter list:')
    s = a.split()
    for i in range(len(s)):
        s[i]=int(s[i])
    isSorted(s)
