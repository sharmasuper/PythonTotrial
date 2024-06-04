tablevalue = input("enter value you want to convert in table  ")

try :
     for i in range(1,11):
          print(f"{i} * {tablevalue} = > {int(i)*int(tablevalue)}")
except Exception as e :
     print("give error ",e)          
       
