def greet(fx) :
    
    def mfx() :
        print('Good Morning')
        fx()
        print('Thanks for using this function')
    return mfx

@greet
def hello() :
    print('hello world') 
@greet #yya greet(hello)()
def add() :
    print("mohit")

add()
hello()





