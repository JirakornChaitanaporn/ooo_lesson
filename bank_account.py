class AccountDB:
    def __init__(self):
        self.account_list = []

    def add_account(self, account):
        if self.search_account_i(account.accNum) == -1:
            self.account_list.append(account)
        else:
            print("Account", account.accNum, "already exists")
            
    def search_account_i(self, num):
        for i in range(len(self.account_list)):
            if self.account_list[i] == num:
                return i
        return -1
    
    def search_acc_obj(self, accNum):
        for account in self.account_list:
            if accNum == account.accNum:
                return account
            else:
                return None
    
    def __str__(self):
        s = ''
        for account in self.account_list:
            s += str(account) + ", "
        return s
    
class Account:
    def __init__(self, accNum, type, name, balance):
        self.accNum = accNum
        self.type = type
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return '{' + str(self.accNum) + ',' + str(self.type) + ',' + str(self.accNum) + ',' + str(self.balance) + '}'
    
account_database = AccountDB()
acc1 = Account("0000", "saving", "David Patterson", 1000)
account_database.add_account(acc1)
acc2 = Account("0001", "checking", "John Hennessy", 2000)
account_database.add_account(acc2)
acc3 = Account("0003", "saving", "Mark Hill", 3000)
account_database.add_account(acc3)
acc4 = Account("0004", "saving", "David Wood", 4000)
account_database.add_account(acc4)
acc5 = Account("0004", "saving", "David Wood", 4000)
account_database.add_account(acc5)


print(account_database)
print(account_database.search_acc_obj('0003'))
account_database.search_acc_obj('0003').deposit(50)
print(account_database.search_acc_obj('0003'))
account_database.search_acc_obj('0003').withdraw( 25)
print(account_database.search_acc_obj('0003'))
# delete_account('0003')
# show_account('0003')
# deposit('0003', 50)
# withdraw('0001', 6000)