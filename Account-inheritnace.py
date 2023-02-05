

#~! FIELDS
#! Account number
#! Holders's name
#! Balance


class Account:

    def __init__(self, ac, hn, bal) -> None:
        self.account_number = ac
        self.holders_name = hn
        self.balance = bal
        self.transactions = []

    #~* DUNDER (Double underscore both side)
    #* They are invoke automatically on certain action
    def __str__(self):
      return f"Account number : {self.account_number} Holder name : {self.holders_name} balance {self.balance}"


    def __repr__(self):
        return f"Account({self.account_number}, \"{self.holders_name}\", {self.balance})"
    

    def __gt__(self, rhs):
        print("__gt__ called", self.holders_name, rhs.holders_name)
        return self.balance > rhs.balance
    
    def __eq__(self, rhs):
        return self.balance == rhs.balance
    
    def print_passbook(self, no_transactions):
        # print("Account number:    ", self.account_number)
        # print("Holder's name      ", self.holders_name)
        # print("Balance            " ,self.balance)  
        # print("Account number: %05d Holder's name: %s Balance: %d" % (self.account_number, self.holders_name, self.balance))
        # print("[{0:20}]".format(self.account_number))
        # > Right align
        #! ^ center align
        #* < left align

        # print("Account number=[{0:^10d}] Holder's name=[{1:^20}] Balance=[{2:^15.2f}]".format(self.account_number, self.holders_name, self.balance))

        print(f"Account number: {self.account_number}\nHolder's name: {self.holders_name}\nBalance: {self.balance:.2f}")
        
        print()
        num = 1
        print("-"*21)
        print(f"num {'Amount':>10} Type")
        print("-"*21)

        transactions = self.transactions[no_transactions:]
        for tran in transactions:
            print(f"{num:003} {tran[0]:10} {tran[1]}")
            num +=1
        print("-"*21)
    def deposit(self, amount):
        self.balance += amount
        tran = (amount, "CR") #? Tuple
        self.transactions.append(tran)

    def withdraw(self, amount):
        self.balance -= amount
        tran = (amount, "DR") #? Tuple
        self.transactions.append(tran)

    def printBalance(self):
        print("Balance:  ", self.balance)


class SavingAccount(Account):

    #~* __init__ of base class gets called automatically
    def __init__(self, ac, hn, bal, min_bal):
        #~? constructor chaining
        super().__init__(ac, hn, bal)   #~-> First call base call
        self.min_balance = min_bal      #~% Then initialize current class

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
           raise Exception('Insufficient balance')
        super().withdraw(amount)


class CurrentAccount(Account):

    def __init__(self, ac, hn, bal, od_limit):
        super().__init__(ac, hn, bal)
        self.overdraft_limit= od_limit


    def withdraw(self, amount):
        if self.balance - amount  < - self.overdraft_limit:
            raise Exception("Overdraft limit reached")
        super().withdraw(amount)


class FixedDeposit(Account):

    def withdraw(self, amount):
       raise Exception('Cannot withdraw from FD')


guido = Account(10010, "Guido van Rossum", 1000000)

# print("Guido passbook")
# guido.print_passbook()
# guido.withdraw(1000000)
# guido.withdraw(10)
# guido.deposit(1900000)
# guido.print_passbook()


print()
# print("Ravi passbook")
# ravi = Account(1000101, "Ravi", 100000)
saving = SavingAccount(1000101, "Ravi", 2000, 1500)
guido = SavingAccount(10100001, 'Guido van Rossum', 2000, 5000)

if saving >= guido:
    print('YES')
else:
    print("No")


# guido.withdraw(1500)
# guido.withdraw(1500)
# guido.withdraw(1500)
# guido.withdraw(1500)
# guido.print_passbook(3)
# ranjan = FixedDeposit(1010000, 'Ranjan', 1)

# print(saving.__init__.__doc__)
# bank_list = [saving]

# for acc in bank_list:
#     try:
#         acc.withdraw(50)
#         acc.print_passbook()
#         print("\n")
#     except Exception as err: 
#         print("Error", acc.holders_name, err)

# ravi.print_passbook()
# ravi.deposit(500)
# ravi.withdraw(500)
# ravi.print_passbook()
# ravi.withdraw(1200)
# ravi.withdraw(3000)
# ravi.withdraw(2000)

# ravi.withdraw(1500)
# ravi.withdraw(1500)
# ravi.withdraw(1)
# ravi.print_passbook()




# print(ravi)
# s = str(ravi)
# print(s)

# #? repr

# print("repr")
# r= repr(ravi)

# print(r)
# obj2 = eval(r)
# obj2.print_passbook()
