import random
size=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
flower=['meihua','hongtao','fangkuai','heitao']
print('The card you picked is the '+size[random.randint(0,len(size)-1)]+' of '+flower[random.randint(0,len(flower)-1)])
