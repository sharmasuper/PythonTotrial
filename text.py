try:

#  f = open('data.txt','r') reading file
#  text = f.read()
#  print(text)

#  f = open('myfile.txt','a')
#  f.write('hello,world  add!')  # new file have create and when we run agin compiler this text agin add myfile.txt
 
#  f.close()
 # new method
 with open('mynewfile.txt','a') as f :
    f.write("Hey I am inside with add")

except Exception as e :
    print("error show",e)
