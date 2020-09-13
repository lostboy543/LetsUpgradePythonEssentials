class BankAccount:
    
    def __init__(self, ownerName, balance):
        self.ownerName = ownerName
        self.balance = balance
    
    def __str__(self):
        return 'Account owner: {ownerName}\nAccount balance: ${balance}'.format(ownerName=self.ownerName, balance=self.balance)
        
    def deposit(self, dp_money):
        self.balance += dp_money
        print('Deposit Accepted, your balance is {balance}'.format(balance=self.balance))
    
    def withdraw(self, wd_money):
        if wd_money > self.balance:
            print('Funds Unavailable!')
        else:
            self.balance -= wd_money
            print('Withdrawal Accepted, your balance is {balance}'.format(balance=self.balance))
            
acct1 = BankAccount('Ram',100)
print(acct1)


acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
