from employee import Employee

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
    def toString(self):
        return ("N:{} Dep:{} Sal:{} Yearly:{}".format(self._name,self._dep,self.__sal,self._sumSal()))
    def toString(self):
        return (super().toString()+" Age:{} Skill:{}".format(self.__age,self._skill))
 
