

class Employees :
    def __init__(self, name, age):
        self.name = name
        self.salary = age
    @classmethod

    def fromstr(cls,string) :
        return cls(string.split("-")[0],string.split("-")[1])

e1 = Employees('Harry',120000)
print(e1.name)  
print(e1.salary) 
string = "John-12000" 
e2 = Employees.fromstr(string)     
print(e2.name)  
print(e2.salary) 


