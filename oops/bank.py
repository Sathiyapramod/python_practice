"""
Create a class called EWallet to manage a digital payment account.

1. Attributes in __init__:
account_holder (string, e.g., "Muthupandi")
balance (integer, e.g., starting at 500)

2. Methods to write:
• add_fund(amount): Adds amount to balance and prints: "Added ₹[amount]. New balance: ₹[balance]".
• withdraw_fund(amount):

Checks if there is enough money in balance.
If balance >= amount:
  Subtracts amount from balance
  and prints: "Withdrew ₹[amount]. Remaining balance: ₹[balance]".

If balance < amount:
 Prints: "Insufficient balance! Cannot withdraw ₹[amount]".
"""


class EWallet:
    # constructor
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.__user_pin = pin

    # methods
    def add_fund(self, amount):
        self.balance = self.balance + amount
        print("Amount credited !!!")
        print("Your New Bank Balance is", self.balance)

    def withdraw_fund(self, amount, pin):
        # compare your pin number with self.__user_pin
        if pin != self.__user_pin:
            print("INCORRECT PIN number")
        else:
            print("PIN number matching")
        if amount > self.balance:
            # amount greater than balance -> Insufficient balance
            print("Insufficient Balance !!, Cannot withdraw", amount)
        else:
            # amount less than balance -> ok go ahead
            # subtract the amount from bank balance
            self.balance = self.balance - amount
            # AMount debited message
            print("Amount debited")
            # Current Balance show
            print("Your Current Bank Balance is", self.balance)


user = EWallet("Muthupandi", 10000, 2233)

print(user.name)
# add 2000
user.add_fund(2000)
user.add_fund(1000)
user.withdraw_fund(amount=5000, pin=1234)
