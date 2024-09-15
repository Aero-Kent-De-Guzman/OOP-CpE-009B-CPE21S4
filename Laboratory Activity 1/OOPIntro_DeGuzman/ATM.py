"""
  ATM.py
"""

class ATM():
  def __init__ (self,
    account = "",
    amount  = 0.0,
    serial_number = 0,
    transactionHistory = {'Chua' : [], 'Doe' : []},
  ):
    self.account = account
    self.amount = amount
    self.serial_number = serial_number
    self.transactionHistory = transactionHistory
  
  def deposit(self, account, amount):
    account.current_balance = account.current_balance + amount
    print("Deposit Complete")
    self.transactionHistory[account.account_lastname].append(amount)

  def withdraw(self, account, amount):
    account.current_balance = account.current_balance - amount
    print("Withdraw Complete")
    amount *= -1
    self.transactionHistory[account.account_lastname].append(amount)

  def check_currentbalance(self, account):
    print(account.current_balance)
    
  def serialcode(self,serial_number):
    if serial_number != 3692:
      return 0
    else:
      return serial_number

  def view_transactionsummary(self, serial_number):
      print('Transaction History')
      print(self.transactionHistory)