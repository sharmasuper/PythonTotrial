# asyncio.Condition method  
# Certainly! The asyncio.Condition class in Python is used to 
# wait for some condition to be met. It works similarly to threading
# .Condition but is designed for use with asyncio's event loop 
# and coroutines.

# asyncio.condition class kai method
# acquire   , notify
# locked , notify_all, locked, release ,wait , wait for


# output is
# Consumer is waiting for condition.
# Producer changed state.value to 1
# Consumer received notification: state.value=1

import asyncio

class SharedState :
    def __init__(self) :
        self.value = 0 

async def consumer(cond,state) :
    async with cond :         
        await cond.wait()
        print(f"Consumer received notified : state.value is {state.value}")

async def Producer(cond,state) :
    await cond.acquire()  # Explicity acquire the condition's lock
    try :
        await asyncio.sleep(1) # Simulate some work 
        state.value +=1 
        print(f"producer changed state.value to {state.value}")
        cond.notify_all()
    finally :     
           cond.release()  # Always release the look 



async def main () :
  cond = asyncio.Condition()
  state = SharedState()
  consumer_task = asyncio.create_task(consumer(cond,state))
  producer_task = asyncio.create_task(Producer(cond,state))
  await asyncio.gather(consumer_task,producer_task)

asyncio.run(main())  






