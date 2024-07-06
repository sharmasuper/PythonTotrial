import asyncio 
async def factorial(n,s):
    if(n<=0):
      return 1
    else :
        e =  n* await factorial(n-1,s)
        await asyncio.sleep(1)
        return e 


async def main() :
     result =  await  asyncio.gather(
                           factorial(5,"a"),
                           factorial(4,"b"),
                           factorial(3,"c"),
                           factorial(2,"d"))
     print(result)

asyncio.run(main())     