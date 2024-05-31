# # tuple is immutable 
# # tup = (1,2,4,3,4,5)
# # print(tup)

# # tup = (1)
# # print(type(tup)) //output - class 'int'
# # so we write comma
# tup = (1,)
# print(type(tup))
# tup = (1,30,33,40)
# # tup[1] = 20
# # print(tup[1])   tuples are imutable we only can get tuple value
# # print(tup[-1]) 
# if 30 in tup :
#     # print("hello yes ")

# countries = ("Spain","Italy","India","EngLand")
# countries2 = ("1","hello","sharma")
# print(countries+countries2)

touple = (0,11,2,3,3,4,3)
tup = touple.count(3)
print(tup)
e = touple.index(3,1,4)
print(e)

print("len of tuple ",len(touple))

# change touple to list 
countries = ("hello","hy","name","MOHIT")
a= list(countries)
print(a) 
# now we can be use it as list mehod
a = set(list)
print(a)







