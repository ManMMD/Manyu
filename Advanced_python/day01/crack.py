import crypt

def testPass(cryptPass):
    salt=cryptPass[0:2]
    dictFile=open('/root/Python/Manyu/data/dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if cryptWord == cryptPass:
            print('[+] Found Password:'+word)
        else:
            print('[-] Password '+word+' Not Found')

def main():
    passFile=open('/root/Python/Manyu/data/passwords.txt')
    for line in passFile.readlines():
        user=line.split(':')[0]
        cryptPass=line.split(':')[1].strip(' ')
        print('[+] Cracking Password For:'+user)
        testPass(cryptPass)

if __name__ == '__main__':
    main()

