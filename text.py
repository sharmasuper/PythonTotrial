import asyncio 

async def my_coroutine() :
    await asyncio.sleep(1)
    print("Coroutine completed")

async def main() :
    coro = my_coroutine()
    future = asyncio.ensure_future(coro)

    # Check if objects are futures 
    print(asyncio.isfuture(coro)) # False, because coro is a coroutine object, not a future
    print(asyncio.isfuture(future)) 
    # print("future",future)  
    # await asyncio.sleep(1)
    await future

if __name__ == '__main__':
    asyncio.run(main())      
