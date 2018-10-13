# _*_coding:utf8-
# 最终目的找到zip的密码
import zipfile
import itertools


def createPassword():
    for i in range(6):
        gentor = (''.join(x) for x in itertools.product('1234567890,./;[]{}:<>?`~!@#$%^&*()_+=-',repeat=i))
        path= '/root/Python/Manyu/data/password.txt'
        with open(path,'a') as f:
            while 1:
                try:
                    f.write('huwang'+next(gentor) + '\n')
                    print('写入成功')
                except Exception as e:
                    print(e)
                    break

if __name__ == "__main__":
    createPassword()
