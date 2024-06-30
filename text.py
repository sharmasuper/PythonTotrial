# asyncio.Condition method  
# Certainly! The asyncio.Condition class in Python is used to wait for some condition to be met. It works similarly to threading.Condition but is designed for use with asyncio's event loop and coroutines.

import asyncio 

class SharedState :
    def __init__(self) :
        self.value = 0

async def consumer(cond,state) :
    async with cond :
         print("Consumer is waiting for condition")
         await cond.wait()
         print(f"Consumer recived notification : state.value = {state.value}")
async def producer(cond,state) :
    async with cond :
        await asyncio.sleep(1) # simulate some work
        state.value += 1
        print(f"Producer changed state.value to {state.value}")
        cond.notify_all() # Notify_all waiting consumers

async def main() :
      cond = asyncio.Condition()      
      state = SharedState()           
      consumer_task = asyncio.create_task(consumer(cond,state))
      producer_task = asyncio.create_task(producer(cond,state))
      await asyncio.gather(consumer_task,producer_task)

asyncio.run(main())





