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