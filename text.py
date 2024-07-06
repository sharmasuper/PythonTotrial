import asyncio 

async def example(lock) :
    print("Acquiring lock")
    await lock.acquire()
    print("Lock acquired")
    try :
        #  Do something protected by the lock 
        print("Critical section")
        await asyncio.sleep(2)
    finally :
            #  Releasing lock 
            print("Releasing lock")
            lock.release()

async def main() :
    # create a lock 
    lock = asyncio.Lock()
    # Run the example function with the lock 
    await asyncio.gather(example(lock),example(lock))

# Run the asyncio event loop
asyncio.run(main())

