import zipfile
import time
from threading import Thread

def extractFile(password):
    path='/root/Python/Manyu/data/Joker.zip'
    zFile=zipfile.ZipFile(path)
    try:
        zFile.extractall(pwd=password)
        print('[+] Found password:'+ password +'\n')
    except Exception as e:
       pass

def main():
    for i in range(6):
        passFile = open('/root/Python/Manyu/data/password'+str(i)+'.txt','r')
        for line in passFile.readlines():
            password = line.strip('\n')
            t = Thread(target=extractFile,args=(zFile,password))
        t.start()
        print  Thread.getName(t) + 'is start'

if __name__ == '__main__':
    main()

