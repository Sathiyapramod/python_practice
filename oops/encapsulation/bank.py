class BankATM:

    def __init__(self, account_holder, pin, balance):
        self.account_holder = account_holder  # 🟢 Public
        self._dispensing_tray_status = "Ready"  # 🟡 Protected (Hardware status)
        self.__pin = pin  # 🔴 Private (Secret PIN)
        self.__balance = balance  # 🔴 Private (Secret Balance)

    def withdraw_cash(self, entered_pin, amount):
        pass

    def __dispense_cash(self, amount):
        pass

    def __verify_pin(self, entered_pin):
        return entered_pin == self.__pin


atm = BankATM("Sathish", 1234, 10000)
atm.withdraw_cash(4321, 2000)
print(atm.account_holder)
print(atm.__balance)
# print(atm._BankATM__balance)
