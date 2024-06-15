import time
import asyncio
async def function1() :
    # time.sleep(3)
    await asyncio.sleep(1)
    return "Mohit function 1"
    print("func 1")

async def function2 () :
    # time.sleep(3)
    await asyncio.sleep(1)
    print("func 2")
    return "Mohit function 2"

async def function3() :
    # time.sleep(3)
    await asyncio.sleep(4)
    print("func 3")     
    return "function 3 function 3" 

async def main() :
  L =await asyncio.gather(function1(),function2(),function3()) 
  print(L) 
#  task = asyncio.create_task(function1())   
 ##  await function1()
#  await function2()
#  await function3()  

asyncio.run(main()) 
  