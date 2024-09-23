#  Create a program in python that satisfies the following:
#    Inheritance, Encapsulation, and Abstraction concept with ADT list
#    Class(Employee: emp_id. emp_name, emp_address, Fulltime: allowance, rate, PartTime: rate)
#    Class(Salary: salary_id, Salary, cut_off_date, days_of_work)

# Encapsulation
class Employee():
  def __init__(self, _name, _address, _id, _salary_id, _cut_off_date):
    self._name = _name
    self._address = _address
    self._id = _id
    self._salary_id = _salary_id
    self._cut_off_date = _cut_off_date
    
  def emp_id(self):
    return self._id
    
  def emp_name(self):
    return self._name

  def emp_address(self):
    return self._address

class Salary(Employee):
  pass
    
  def days_of_work(self, x = 30):
    return x - self._cut_off_date

# Inheritance
class Fulltime(Salary):
  def __init__(self, _name, _id, _address, _allowance, salary_id, _Salary, _cut_off_date):
    Salary.__init__(self, _name, _address, _id, salary_id, _cut_off_date)
    self._allowance = _allowance
    self._Salary = _Salary
    
  def fullTime_Salary(self):
    return self._Salary + self._allowance

class PartTime(Fulltime):    
  def __init__(self, _name, _id, _address, _rate, salary_id, _days_of_work, _cut_off_date):
    Salary.__init__(self, _name, _address, _id, salary_id, _cut_off_date)
    self._rate = _rate
    self._days_of_work = _days_of_work
    
  def partTime_Salary(self):
    return self._rate * self._days_of_work

# Abstraction with ADT List
fullemploy = Fulltime('Michael Anderson',
                      142167,
                      '536 Vineyard Road',
                      2500,
                      1,
                      5000,
                      25)
partemploy = PartTime('Jonathan Smith',
                      161260,
                      '7115 Orchard Street',
                      100,
                      2,
                      30,
                      27)

#full time
print('+-full time employee-+\n\n name:', fullemploy._name, "| id:",fullemploy._id, "| address:", fullemploy._address)
print('\n  cutoff date :', fullemploy.days_of_work())
print('  expected salary :', fullemploy.days_of_work())

#part time
print('\n+-part time employee-+\n\n name:', partemploy._name, "| id:",fullemploy._id, "| address:", fullemploy._address)
print('\n  cutoff date :', partemploy.days_of_work())
print('  expected salary :', partemploy.partTime_Salary())