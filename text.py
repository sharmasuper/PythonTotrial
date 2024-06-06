try:
    double = lambda arguments: arguments*2
    avg  = lambda x,y : (x+y)/2
    cube = lambda three : three**3
    print(double(5)) 
    print(cube(5))
    print(avg(3,5))
    # what is Annoymous - 
    # those function called Annoymous ,which does not know about name 

except Exception as e :
    print("add Error",e)    