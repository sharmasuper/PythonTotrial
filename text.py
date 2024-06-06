try :
    f = open('myfile.txt','r')
    i =0
    while True:
        i=i+1
        line = f.readline()
        m1 =  line.split(",")[0]
        m2 =  line.split(",")[1]
        m3 =  line.split(",")[2]
        print(f"Marks of student {i} in maths {m1}")
        print(f"Marks of student {i} in Englisj {m2}")
        print(f"Marks of student {i} in sst {m3}")
        if not line :
           break
        print(line)        
except Exception as  e:
    print("show  error",e) 


#second method use writefile method
try :
  f = open('myfile.txt','w')
  lines = ['line1 \n','line2 \n','line3 \n']
  f.writelines(lines)  
  f.close()

except Exception as e :
    print("add Error",e)    













