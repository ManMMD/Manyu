import time
 
now=time.time()
print(now)
mon=time.localtime(now)[1]
day=time.localtime(now)[2]
year=time.localtime(now)[0]
hour=time.localtime(now)[3]
mins=time.localtime(now)[4]
sec=time.localtime(now)[5]

print('Current date and time is '+str(mon)+' '+str(day)+','+str(year)+' '+str(hour)+':'+str(mins)+':'+str(sec))
