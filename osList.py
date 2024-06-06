import os
try:

  folders = os.listdir('data')
#   print(folders)
  print(os.getcwd()) #own directory check
  os.chdir("/Users")
  print(os.getcwd())
#   print(os.)
#   for i in folders:
#     print(i)
#     print(os.listdir(f"data/{i}"))
except Exception as e :
    print(e)