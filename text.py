difference between is operator and ==
is operator - is operator check exact memory location
== operator - == operator check only value
a = 4
b = "4"
print( a is b) #fasle exact location on memory
print(a == b)  #fasle value

a = [1,2,43]
b = [1,2,43]
print(a is b) #false
print(a == b) #true

a = 3
b = 3
print(a is b)
print(a == b)

a = (1,2)
b = (1,2)  #beacause touple is immutable
print(a is b)
print(a == b)










