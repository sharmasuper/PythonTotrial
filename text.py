class Employee :
    def __init__(self,name) :
        self.name = name
    def show(self) :
        print(f"the name is {self.dancer}")

class Dancer :
    def __init__(self,dance) :
      self.dancer = dance  
    def show(self) :
        print(f"the dancer is {self.dancer}")
class DancerEmployee(Employee,Dancer) :
    def __init__(self,dancer,name) :
        self.dancer = dancer
        self.name = name
    def __str__(self) :
        return f"{self.dancer} and {self.name}"    
  
obj = DancerEmployee("priyanka",'Karthak')  
obj.show()  # jo function pahalai hoga vo pahlai ayga
# in this condition we need mro() method 
print(DancerEmployee.mro())

