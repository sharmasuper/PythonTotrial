# Walrus Operator
a = True
# print(a=False) invalid
print(a:= False)  # outout - false

numbers = [1,2,3,4,5]
while(n:= len(numbers))>0 :
    print(n)
    numbers.pop()
foods = list()
while True :
    food = input("What food ")    
    if food == "quit" :
        break 
    foods.append(food)

print( "print add",foods)    