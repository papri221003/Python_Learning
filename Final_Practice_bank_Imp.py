class Bank:
    
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
        
    #Debit method
    
    def debit(self,amount):
        self.balance-=amount
        print("Rs:",amount,"has been debited from your acc: ",self.acc_no)
        print("Available balance: ",self.get_balance())
        
    #credit
    def credit(self,amount):
        self.balance+=amount
        print("Rs:",amount,"has been credited to your  acc: ",self.acc_no)
        print("Available balance: ",self.get_balance())
        
    def get_balance(self):
        return self.balance
    
b1=Bank(458796,500)

print(b1.get_balance())
b1.credit(500)
b1.debit(100)