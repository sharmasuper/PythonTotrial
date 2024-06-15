# Generators in python are special type of function that allow you to create an iterators sequence of value. 
# A Generators function return a generatos object .
# which can be used to generate the value one-by-one as you iterate over it.
# Generators are a powerful tool for working with large or complex data sets, as they allow ypu to generate the value
# on - the fly , rather than having to create and store the entire sequence in memory

# yeild method-  yeild method create a generator and return a suspended execution 
# ex- 
def my_generator():
    for i in range(5):
        yield i  
gen =  my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))









