

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
    
    
    def print_passbook(self):
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
        for tran in self.transactions:
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

guido = Account(10010, "Guido van Rossum", 1000000)

# print("Guido passbook")
# guido.print_passbook()
# guido.withdraw(1000000)
# guido.withdraw(10)
# guido.deposit(1900000)
# guido.print_passbook()


print()
print("Ravi passbook")
ravi = Account(1000101, "Ravi", 100000)
# ravi.print_passbook()
ravi.deposit(5000)
ravi.withdraw(1000)
ravi.print_passbook()


# print(ravi)
# s = str(ravi)
# print(s)

# #? repr

# print("repr")
# r= repr(ravi)

# print(r)
# obj2 = eval(r)
# obj2.print_passbook()
