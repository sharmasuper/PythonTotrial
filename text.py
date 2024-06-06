try :
    def cube(x) :
        return x**3
      
    
    newl = [1,2,3,4,5,6]
    # nell = []
    # for i in newl :
    #     nell.append(cube(i))
    # print(nell)  
    # Map(function,item) method //item - one by one take item
    newl2 = list(map(cube,newl))
    print(newl2)

    #filter
    def filter_function (a) :
        return a>4
    newnewl = list(filter(filter_function,newl))
    print(newnewl)


# except Exception as e :
#     print("add Error",e)

#reduce funciton 

try:
    from functools  import reduce
    numbers = [1,2,3,4,5]
    def mysum(x,y) :
      return x + y
      #reduce(function,element,starting value)
    sum = reduce(mysum,numbers,5)  
    print('sum',sum) 

except Exception as e :
    print("add Error",e)    




