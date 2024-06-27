import asyncio 
async def coroutine1() :
    print('Coroutine 1 is starting')
    await asyncio.sleep(1)
    print('Coroutine 1 is done')

async def coroutine2() :
    print('Coroutine 2 is startine')
    await asyncio.sleep(1)
    print('Coroutine 2 is done')

# create a event loop

async def main() :
    print('Creating tasks')
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())

    print('Tasks created , waiting for completion')
    await asyncio.gather(task1,task2)

# Run the event loop 

if __name__ == '__main__':
    asyncio.run(main())





