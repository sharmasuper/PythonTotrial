ep1 = {122:45,123:89,567:69,670:69}
ep2 = {22:67,566:90}
ep1.update(ep2)
print(ep1)
# print(ep2)
# ep1.clear()
# print(ep1)
ep1.popitem() # last item delete
print(ep1)

del ep1[122]
print(ep1)