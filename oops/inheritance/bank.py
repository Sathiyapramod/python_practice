class Bank:

  def __init__(self,card,password):
    self.card = card
    self.password = password
    self.balance = 10000
  
  def check(self):
  
    card = 1234
    password = 4321

    if self.card == card and self.password == password:
      a = input("enter the payment method (deposit ,widthraw,balance) : ")
      if a == "deposit":
        b = int(input("enter the amount : "))
        self.__deposit(b)
      elif a == "widthraw":
        b = int(input("enter the amount : "))
        if self.balance >= b:
          self.__Widthraw(b)
        else:
          print("insuffient balance")
      elif a == "balance":
        print("Your account Balance : ",self.balance)
    else:
      print("invaild card or pass")

  def __Widthraw(self,amount):
    self.balance = self.balance-amount
    print("Amount Widthrawed")
    print("cureent balance : ", self.balance)
  def __deposit(self,amount):
    self.balance = self.balance+amount
    print("Amount Deposited")
    print("cureent balance : ", self.balance)

card = int(input("Enter card number : "))
pin = int(input("Enter upi pin : "))
bank = Bank(card,pin)
bank.check()