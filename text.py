import asyncio

async def waiter(event) :
    print('Waiting for the event to the set')
    await event.wait()
    print("Event has been set !")

async def setter(event):
    print("setting the event in 2 second")
    await asyncio.sleep(2)
    event.set()
    print("Event has been set!")

async def main() :
    event = asyncio.Event()
    waiter_task = asyncio.create_task(waiter(event))
    setter_task = asyncio.create_task(setter(event))
    await asyncio.gather(waiter_task,setter_task)

asyncio.run(main())
