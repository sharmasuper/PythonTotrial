# # # set method
# # s1 = {1,2,5,6}
# # s2 = {3,6,7}
# # # union method
# # print(s1.union(s2))  
# # s1.update(s2)
# # print(s1)
# # # difference between upadte method and union method is - 
# # s = s1.union(s2)
# # print(s)

# # s1.update(s2)
# # print(s1)

# # # intersection method
# # cities = {"Tokyo","Madrid","Berlin","Delhi"}
# # cities2 = {"Tokyo","seoul","kabul","Madhrid"}
# # cities3 = cities.intersection(cities2)
# # print(cities3)
# # # intersection, this method gives which value are both common in cities and cities2 set
# # semitric difference
# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# # cities3 = cities.symmetric_difference(cities2)
# # print(cities3) 

# # output - {'Delhi', 'Berlin', 'Seoul', 'Kabul'}
# # cities3 = cities.difference(cities2)
# # print(cities3) 
# # print(cities.isdisjoint(cities2))  if everyone element does not match both of them it return true
# cities3 = {"Tokyo","Madrid","Delhi"}
# print(cities.issuperset(cities3))
# # it means cities3 elements are in cities if it have it give true else false

# print(cities3.issubset(cities))  


# cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities.remove('Tokyo')  it give error when element does not match
# print(cities)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
# cities.discard('Tokyo2')  it not give error when element does not match
# print(cities)
a = cities.pop()
print(a)
print(cities)
del cities
print(cities)





