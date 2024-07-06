# The asyncio.Future class in Python is used to represent an eventual
#  result of an asynchronous operation. It's part of the asyncio 
#  module, which is used for writing concurrent code using the 
#  async/await syntax.

import asyncio 

async def set_future_value(fut) :
    # await asyncio.sleep(2)
    fut.set_result('! future is done')

async def main() :
    loop = asyncio.get_running_loop()
    fut = loop.create_future()

    asyncio.create_task(set_future_value(fut))     
    result = await fut 
    print(result)

asyncio.run(main())

