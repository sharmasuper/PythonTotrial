import asyncio 

async def main() :
    # create a future object 
    future = asyncio.Future()
    # Get the event loop associated with the Future 
    loop = future.get_loop()
    # Print the event loop 
    print(f"The event loop for this future is : {loop}")
    # Schedule a task that will complete the future after a delay 
    asyncio.create_task(complete_future(future)) 

    await future
    print(f"future result : {future.result()}")

async def complete_future(future) :
    await asyncio.sleep(2) 
    future.set_result("Task completed successfully") 

asyncio.run(main())       

