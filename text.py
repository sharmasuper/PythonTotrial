# list method
L = [11,45,1,2,4,6]
# print(L)
# L.append(3)
# print(L)
# print(L.index(3))
# print(L.count(2))
# difference between copy method

# m = L
# m[0] = 0
# print(m)
# print(L) you looked, frist element of both element are changed
# but if we will use copy mehod, frist list will not change
# m = L.copy()
# m[0] = 0
# print(L)
# print(m)

# L.insert(index,element)
# L.insert(1,99)
# print(L)

# extend
m = [900,1000,1100]
# L.extend(m)
# print(L)

K = L+m
print(K)




