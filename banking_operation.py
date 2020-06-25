import sys
class Bank():
    '''The most common banking operation performed'''
    bankname='ANZA Bank'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('The current balance is:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('Withdrawal amount exceeding the current balance')
            sys.exit(0)
        else:
            self.balance=self.balance-amt
            print('The balance after withdrawing is:',self.balance)
name=input('please enter your name:')
a=Bank(name)
print('Welcome to',Bank.bankname)
while True:
    print('d=Deposit\nw=Withdraw\ne=Exit')
    option=input('Kindly enter the desired operation:')
    if option=='d' or option=='D':
        amt=float(input('Please enter the deposit amount:'))
        a.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('Enter the amount to be withdrawan:'))
        a.withdraw(amt)
    elif option=='e' or option=='E':
        print('Thank you for banking with ANZA bank')
        sys.exit(0)
    else:
        print('Please enter a valid option')
