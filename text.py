# The add_done_callback method in asyncio.Future allows you to attach
#  a callback function that will be called when the Future is done 
#  (either successfully or with an exception).

import asyncio 

def done_callback(fut) :
    print(f"future is done {fut.result()}")

async def set_future_value(fut) :
    await asyncio.sleep(1)
    fut.set_result("future is done !")
    print("future value set") 

async def main() :
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    fut.add_done_callback(done_callback)
   
    asyncio.create_task(set_future_value(fut))
    result = await fut 
    print(f" main done with result : {result}")


asyncio.run(main())


    



