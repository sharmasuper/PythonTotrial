info = {'name' : "Karna","age":"19","eligible":True}
print("dic pri",info)
print(info['name'])  #yai error show kartha h element nahi honai per
print(info.get('name2')) #yai error show nahi kartha 
print(info.keys()) # these method we get all keys
print(info.values())
# for key in info.values() :# info.keys()
#     # print(info[key])
#     # print(value)
#     print(key)
   
for key,value in info.items() :
    print(key)
    print(value)



