try :
    
     with open('data.txt','r') as f :
        print(type(f))
        #Move to the 10th byte in the file
        f.seek(10)
        # data f.read()
        print(f.tell())
        data = f.read(5)
        print(f.tell())  #whenever to seek
       
        #Read the next 5 bytes
        print(data)
        #second method
       with open('Sample.txt','w') as f :
        f.write("Hello World !")
        f.truncate(5) # means 5 len limit will print world
       with open('Sample.txt','r') as f :
        print(f.read()) 

except Exception as e :
    print("add Error",e)    