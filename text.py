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
            print("Consumer waiting for condition")
            await cond.wait()
            print(f"Consumer recived notificaiton value is state.value = {state.value}")


async def producer(cond,state) :
        await asyncio.sleep(1)
        async with  cond :
            state.value += 1
            print(f"Producer changed state.value to {state.value}")
            #cond.notify() # Notify one waiting consumer 
            cond.notify_all() # Uncoment to notify all waiting consumers

async def main() :
    cond = asyncio.Condition()
    state = SharedState()

    consumer_task = asyncio.create_task(consumer(cond,state))
    prodcer_task = asyncio.create_task(producer(cond,state))
    await asyncio.gather(consumer_task,prodcer_task)
asyncio.run(main())     
