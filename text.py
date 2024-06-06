import  os

# if(not os.path.exists('data')):    
# os.mkdir('data')
try :
   for i in range(0, 100):
      os.rename(f"data/day{i+1}.txt",f"data/mohit{i+1}.txt") 

except Exception as e :
     print("add",e)






