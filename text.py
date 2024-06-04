def funck1():
 try :
    l = [1,2,3,4]
    i = int(input("Enter the Index "))
    print(l[i])
    return "true"
 except : 
      print('Some error find') 
      return 0
# except Exception as e :
#      print("some error find",e)
 finally : 
      print("i am always excecuted")      #it return karai jab bhi excecute hoga jabki easi print mai likhnai per exceute nahi hoga   
      return "hel"
 print("i am always executed")

val = funck1()
print(val)