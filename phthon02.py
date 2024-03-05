class Employee:
     #class variable ใช้งานโดยไม่ต้องสร้าง obj
    __minSal = 15000
    _maxSal = 50000
    
    def __init__(self,name,sal,dep):
        print ("===Welcome===")
        self.__sal = sal #private
        self._dep = dep
        self._name = name #protected

    def _showData(self):
        print("Name: {}".format(self._name))
        print("Salary: {}".format(self.__sal))
        print("Departmen: {}".format(self._dep))
        print("All data:",format(self.getN()))
    
    def _sumSal(self):
        return self.__sal*12
    #setter
    def setN(self,newname,newsal):
        self._name = newname
        self.__sal = newsal
        
    def toString(self):
        return ("N:{} Dep:{} Sal:{} Yearly:{}".format(self._name,self._dep,self.__sal,self._sumSal()))
        
    def __del__ (self):
        print ("===End===")

    #getter
    def getN(self):
        return self._name, self.__sal
    
   

# emp1.detail("kim",30000)
# emp1._name = "ky"
# emp1.__sal = 50000
# emp1._showData()
# print ("Min:",Employee._minSal, "Max:", Employee._maxSal)
# print (isinstance(emp1,Employee))
# print (isinstance(emp1,int))
# print (dir(emp1))
# print (emp1.__class__)


class Accounting(Employee):
    _dep = "Acc"
    def __init__(self,name,sal,age):
        super().__init__(name,sal,self._dep)
        self.__age = age
    def _showData(self):
        super()._showData()
        print("Age: {}".format(self.__age))
    def showA(self):
        return print("A")
    def showA(self,B):
        return print("B")

class Programmer(Employee):
    _dep = "IT"
    def __init__(self,name,sal,age,skill):
        super().__init__(name,sal,self._dep)
        self._skill = skill
        self.__age = age
    def _showData(self):
            super()._showData()
            print("Skill: {}".format(self._skill))
            print("Age: {}".format(self.__age))


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
