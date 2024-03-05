from employee import Employee
from account import Accounting
from programmer import Programmer

# emp1.detail("kim",30000)
# emp1._name = "ky"
# emp1.__sal = 50000
# emp1._showData()
# print ("Min:",Employee._minSal, "Max:", Employee._maxSal)
# print (isinstance(emp1,Employee))
# print (isinstance(emp1,int))
# print (dir(emp1))
# print (emp1.__class__)

emp1 = Employee("Ben",20000,"CEO")
emp2 = Accounting("Kim",30000,35)
emp3 = Programmer("Brad",35000,30,"Coding")

# (emp1._showData())
# (emp2._showData())
# (emp3._showData())
print(emp1.toString())
print(emp2.toString())
print(emp3.toString())

# print("Min:",emp2._Employee__minSal)
# print("Yearly income:",emp2._sumSal())
# print("Max:",emp3._maxSal)
# print("Emp3 =",emp3.toString())
# print(emp1.toString())