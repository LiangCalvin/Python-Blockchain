from employee import Employee

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
    def toString(self):
        return (super().toString()+" Age:{}".format(self.__age))
 