class Account:
    def __init__(self,id=0,balance=100,annuallnterestRate=0):
        self.__id=id
        self.__balance=balance
        self.__annuallnterestRate=annuallnterestRate/100
    def getMonthlyInterestRate(self):
        monthlyinterestRate=self.__annuallnterestRate/12
        print('MonthlyInterestRate:'+str(monthlyinterestRate))
    def getMonthlyInterest(self):
        monthlyinterest=self.__balance*(self.__annuallnterestRate/12)
        print('MonthlyInterest:'+str(monthlyinterest))
    def withdraw(self,w):
        self.__balance=self.__balance-w
    def deposit(self,d):
        self.__balance=self.__balance+d

m=Account(1122,20000,4.5)
m.withdraw(2500)
m.deposit(3000)
print('ID:'+str(m._Account__id)+'\nBalance:'+str(m._Account__balance))
m.getMonthlyInterestRate()
m.getMonthlyInterest()

