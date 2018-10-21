# _*_coding:utf8-
# 最终目的找到zip的密码
import zipfile
import itertools


def createPassword():
    gentor = (''.join(x) for x in itertools.product('0123456789.',repeat=4))
    path= '/root/Python/Manyu/data/password.txt'
    with open(path,'a') as f:
        while 1:
            try:
                f.write('Huwang'+next(gentor) + '\n')
                print('写入成功')
            except Exception as e:
                print(e)
                break

if __name__ == "__main__":
    createPassword()
