class Bankaccount:
    def __init__(self, owner, amount):
        self.owner = owner
        self._account_type = "current"
        self.__balance = amount
    @property
    def balance(self):
        return self.__balance
    
    def deposit_amount(self , amount):
        if amount>0:
            self.__balance += amount
            print(f" RS. {amount} deposited successfully ")
        else:
            print("invalid deposit")
    def withdraw_balance(self , amount):
        if amount >self.__balance:
           print(f"Transaction failed! your balance is:{self.__balance}")
        elif amount<=0:
           print("Invalid withdraw mount!")
        else:
           self.__balance -= amount
           print(f"RS. {amount} successfully withdraw")
account = Bankaccount("kinza " , 5000)
account.deposit_amount(7000)
print(f"your current balance is:{account.balance}")
account.withdraw_balance(8000)
