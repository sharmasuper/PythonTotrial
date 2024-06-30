# coroutine acquire()method example in python
#asyncio.Condition.asquare() method
# The acquire() method in asyncio is used with synchronization 
# primitives such as asyncio.Lock, asyncio.Semaphore, and 
# asyncio.Condition to acquire the lock or semaphore.
 
import asyncio
async def worker(lock,worker_id) :
    print(f"Worker {worker_id} is waiting to acquire the lock")

    async with lock :
        print(f"worker {worker_id} has acquired the lock")
        await asyncio.sleep(1)
    print(f"Worker has released the lock {worker_id}")

async def main() :
    lock = asyncio.Lock()
    for i in range(3):
     await asyncio.gather(worker(lock,i))

     


asyncio.run(main())    





