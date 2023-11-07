class caluculation:
    def add(self,a:int,b:int,c:int):
        print(a+b)
    def add(self,a:int,b:int,c:int=0):
         print(a+b+c)
cal=caluculation()
cal.add(1,2,3)


#methodoverriding
class employee:
    __amt=20000
    def sal(self):
        return self.__amt*12
class contractemploye(employee):
        __hrpay=1000
        __hrs=10
        def salary(self):
            return self.__hrpay*self.__hrs
emp=contractemploye()
print(emp.sal())

#default constructer

class Employee:
    def fullName(self,fName,lName):
        print(fName+lName)
emp=Employee()
emp.fullName("ahmed", "pasha")

#perameterless constructer

class Employee:
    def __int__(self):
        pass
    def fullName(self,fName,lName):
        print(fName+lName)
emp=Employee()
emp.fullName("ahmed","pasha")

#paramenterized constructer

class employee:
    __fname:str=""
    __lname:str=""
    def __init__(self,fName,lName):
        self.__fname=fName
        self.__lname=lName
    def fullName(self):
         print(self.__fname +" "+ self.__lname)
emp=employee("ahmed","pasha")
emp.fullName()
