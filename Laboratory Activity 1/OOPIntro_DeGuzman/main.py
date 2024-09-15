"""
  main.py
"""
import Accounts
import ATM

Account1 = Accounts.Accounts(
  account_firstname = 'Royce',
  account_lastname  = 'Chua',
  current_balance   = 1000,
  address           = 'Silver Street Quezon City',
  email             = 'roycechua123@gmail.com'
) # create the instance/object

Account2 = Accounts.Accounts(
  account_firstname = 'John',
  account_lastname  = 'Doe',
  current_balance   = 2000,
  address           = 'Gold Street Quezon City',
  email             = 'johndoe@gmail.com'
)

ATM1 = ATM.ATM()
ATM1.deposit(Account1,500)
ATM1.withdraw(Account1,1018)
ATM1.deposit(Account1,1631)
ATM1.withdraw(Account1,721)
ATM1.deposit(Account2,300)
ATM1.deposit(Account2,671)
ATM1.withdraw(Account2,914)
ATM1.deposit(Account2,1148)

n = int(input('\nSERIAL NUMBER FOR THE ATM\n\t"3692"\n\nPlease input a serial number to initialize ATM: '))
x = ATM1.serialcode(n)

while x == 0:
  print('\n#########################\n  INVALID INPUT\n#########################\n')
  n = int(input('SERIAL NUMBER FOR THE ATM\n\t"3692"\n\nPlease input a serial number to initialize ATM: '))
  x = ATM1.serialcode(n)

print('\n#########################\n  Account 1 Details\n#########################\n')
print('firstname\t\t:',Account1.account_firstname)
print('lastname\t\t:',Account1.account_lastname)
print('current balance\t:',Account1.current_balance)
print('address\t\t\t:',Account1.address)
print('email\t\t\t:',Account1.email)
print('\n#########################\n  Account 2 Details\n#########################\n')
print('firstname\t\t:',Account2.account_firstname)
print('lastname\t\t:',Account2.account_lastname)
print('current balance\t:',Account2.current_balance)
print('address\t\t\t:',Account2.address)
print('email\t\t\t:',Account2.email)
print('\n#########################\n')
ATM1.view_transactionsummary(x)
print('\n#########################\n  serial number : ', x ,'\n#########################\n')