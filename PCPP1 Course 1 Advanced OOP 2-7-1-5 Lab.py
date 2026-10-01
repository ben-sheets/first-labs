class AccountError(Exception):
    pass


class SingleBankAccount:
    def __init__(self, AccountNumber):
        self.__number = AccountNumber
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            if new_balance - self.__balance > 100:
                print("Deposit greater than $100!")
            if self.__balance - new_balance > 100:
                print("Withdrawal greater than $100!")
            self.__balance = new_balance
        else:
            raise AccountError

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, NewAccountNumber):
        raise AccountError

    @number.deleter
    def number(self):
        if self.__balance == 0:
            self.__number = None
        else:
            raise AccountError

print("Begin testing...")
print("Creating account number 12345...")
test = SingleBankAccount(12345)
print("Account", test.number, "balance is: ", test.balance)
test.balance = 1000
print("Account", test.number, "balance is: ", test.balance)
test.balance = 1001000
print("Account", test.number, "balance is: ", test.balance)
try:
    print("Attempting to set balance to -$200...")
    test.balance = -200
    print("Account", test.number, "balance is: ", test.balance)
except AccountError as e:
    print("Balance can't be negative")

try:
    test.number = 5678
    print("Account", test.number, "balance is: ", test.balance)
except AccountError as e:
    print("Can't change account numbers!")

try:
    del test.number
    print("Account", test.number, "balance is: ", test.balance)
except AccountError as e:
    print("Can't delete an account with non-zero balance!")


