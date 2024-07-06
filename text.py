# The asyncio.Future.cancel() method is used to cancel a Future in Python's asyncio library. 

import asyncio 

async def main() :
    future = asyncio.Future()
    # Schedule a task to complete the future after a delay
    asyncio.create_task(complete_future(future))
    #cancel the future before it is completed 
    await asyncio.sleep(1)
    future.cancel()

    try : 
        # Await the future to raise the cancellation exception
        await future 
    except asyncio.CancelledError :
         print('Future was cancelled')


async def complete_future(future):
    await asyncio.sleep(2)
    if not future.cancelled():
        future.set_result("Future is done!")
    

asyncio.run(main())






