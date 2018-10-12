import crypt
import itertools

def main():
    flag=0
    salt='AB'
    cryptPass='AB5I64J9ZNvp2'
    #test=(''.join(x) for x in itertools.product("huwangW", repeat=7))
    test=(''.join(x) for x in itertools.product("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM", repeat=7))
    while flag==0:
        word=next(test)
        cryptWord = crypt.crypt(word,salt)
        if cryptWord == cryptPass:
            print('[+] Found Password:'+word)
            flag=1
        elif cryptWord == 'ABwpCvqmz77No':
            print('[-] Not Found')

if __name__ == '__main__':
    main()

