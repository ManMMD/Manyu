def eliminateDuplicates(lst):
    s=[]
    for i in lst:
        if i not in s:
            s.append(i)
    print(s)

if __name__ == '__main__':
    a=raw_input('Enter ten number:')
    l=a.split()
    eliminateDuplicates(l)
