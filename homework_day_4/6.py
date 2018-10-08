def numberOfDaysInAYear(year):
    if (year%4==0) and (year%100!=0) or (year%400==0):
        print(str(year)+'  364')
    else:
        print(str(year)+'  365')

for i in range (2010,2021):
    numberOfDaysInAYear(i)
