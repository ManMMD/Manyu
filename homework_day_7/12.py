def isConsecutiveFour(values):
    flag = 0
    print(len(values))
    if len(values)>=4:
        for i in range(len(values)-3):
            if values[i]==values[i+1] and values[i]==values[i+2] and values[i]==values[i+3]:
                flag = 1
                break
            else:
                flag = 0
        if flag == 1:
            print('Yes')

        else:
            print('No')
    else:
        print('No')


if __name__ == '__main__':
    a=raw_input('>>')
    s=a.split()
    for i in range(len(s)):
        s[i]=int(s[i])
isConsecutiveFour(s)
