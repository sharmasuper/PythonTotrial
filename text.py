# In Python's asyncio module, the Task class is used to wrap 
# coroutines in a way that they can be run concurrently as part of an
#  event loop. This class allows you to schedule coroutines and manage
#   their execution.

import asyncio

async def coro1() :
    for i in range(3) :
        print(f"coro1 iteration {i}")
        await asyncio.sleep(1) 

async def coro2() :
    for i in range(3) :
        print(f"coro2 iteration {i}")
        await asyncio.sleep(1.5)

async def main() :
    # Get the current event loop 
    # loop = asyncio.get_event_loop()
    # Create a tasks using asyncio.Task 
    # task1 = asyncio.Task(coro1(),loop=loop,name ="task1")
    # task2 = asyncio.Task(coro2(),loop=loop,name='task2') 
    # esai bhi kar sktai h
    task1 = asyncio.create_task(coro1())
    task2 = asyncio.create_task(coro2())
    await asyncio.gather(task1,task2)

if __name__ == "__main__" :
  asyncio.run(main())    

  








