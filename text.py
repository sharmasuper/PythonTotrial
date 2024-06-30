import asyncio
class SharedResource :
    def __init__(self) :
        self.resource = None
        self.condition = asyncio.Condition()

    async def producer(self) :
        async with self.condition :
            print('Producer : Producing resource') 
            self.resource = "Resource data"
            self.condition.notify_all()

    async def consumer(self,consumer_id) :
        async with self.condition :
            print("consumer resource")
            await self.condition.wait_for(lambda :self.resource is not None )
            print(f"Consumer {consumer_id} : Consumer resource : {self.resource} ")

async def main() :
    shared = SharedResource()
    producer_task = asyncio.create_task(shared.producer())
    consumer_task = [asyncio.create_task(shared.consumer(i)) for i in range(3)]
    await producer_task
    await asyncio.gather(*consumer_task)   

asyncio.run(main())
        