# #Time module
# import time
# def usingWhile () :
#     i = 0
#     while i<5000 :
#         i = i+1
#         print(i)

# def usingFor() :
#     for i in range(5000) :
#         print(i) 


# init = time.time() # return the time in second
# usingFor()
# t1 = time.time() - init
# init = time.time()
# # print(time.time()-init)
# # end = time.time()
# usingWhile()
# print(time.time() - init)
# print(t1)

# import time
# print(4)
# time.sleep(3)
# print("this is printed after 3 seconds")


import time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)



