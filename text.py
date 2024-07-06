# The asyncio.Future.done() method is used to check if a Future object has been completed, either by setting a result or by being canceled. Here's an example to illustrate its usage

# import asyncio 

# async def main() :
#     # create a Future object
#     future = asyncio.Future()
#     # Schedule a task to complete the future after a delay 
#     asyncio.create_task(complete_future(future)) 
#     # Check if the future is done before it is complted 
#     print(f"Is the future done? {future.done()}")
#     # await the future to be completed 
#     await future 
#     # check it the future is done after it is completd 
#     print(f"Is the future done? {future.done()}") 

#     #Print the result of the future 
#     print(f"future result : {future.result()}")

# async def complete_future(future):
#     await asyncio.sleep(1)
#     future.set_result("Future is done ")

#      # Run the event loop
# asyncio.run(main()) 
# second method 

import asyncio 

async def complete_task(future) :
      future.set_result("future is done ")
      asyncio.sleep(1) 
async def main() :
    loop = asyncio.get_running_loop()
    # create a Future object 
    future = loop.create_future() 
    t_ask = asyncio.create_task( complete_task(future))
    await asyncio.gather(t_ask)
    fu =  future.result()
    print(fu)
    print(f"Is the future done? {future.done()}")  


asyncio.run(main())    
    







      
