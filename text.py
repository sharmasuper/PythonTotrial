# The asyncio.as_completed function in Python is used to create an 
# iterator that yields tasks as they are completed. This can be 
# particularly useful when you have multiple asynchronous tasks and
#  you want to process their results as soon as they become available,
#   rather than waiting for all tasks to complete.

import asyncio
import random
async def my_coroutine(id,delay) :
    print(f"Coroutine {id} started , will sleep for {delay} seconds")
    await asyncio.sleep(delay)
    print(f"Coroutine {id} finished")
    return id

async def main() :
    tasks = [my_coroutine(i,random.randint(1,5)) for i in range(5)]
    for task in asyncio.as_completed(tasks) :
        result = await task 
    print(result)
    # print(f"coroutine {result} has completd.")

asyncio.run(main())        






