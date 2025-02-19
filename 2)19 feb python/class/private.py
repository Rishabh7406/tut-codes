class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # Controlled access

account = BankAccount(1000)
print(account.get_balance())  # ✅ Allowed
# print(account.__balance)  ❌ Error: Cannot access private variable
