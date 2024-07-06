# In Python's asyncio module, the asyncio.Lock class provides a 
# mechanism to manage access to shared resources in asynchronous 
# code. The locked() method of asyncio.Lock is used to check if the 
# lock is currently held by any coroutine. Here's an example 
# demonstrating the usage of locked():

import asyncio 

async def example(lock) :
    if lock.locked():
        print("Lock is currently held by another coroutine")
    else :
        print("Lock is not held ,acquiring")
        await lock.acquire()
        print("Lock acquired successfully") 

        try : 
            #  Simulate some work 
               await asyncio.sleep(2)
        finally : 
                 print("Releasing lock")
                 lock.release()    
async def main() :
     # Create a lock 
     lock = asyncio.Lock()
     task1 = asyncio.create_task(example(lock))
     task2 = asyncio.create_task(example(lock)) 
     await asyncio.gather(task1,task2) 

asyncio.run(main())


