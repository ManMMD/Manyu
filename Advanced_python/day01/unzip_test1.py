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
    passFile = open('/root/Python/Manyu/data/password.txt','r')
    for line in passFile.readlines():
        password = line.strip('\n')
        extractFile(password)

if __name__ == '__main__':
    main()
