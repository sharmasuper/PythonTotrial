import asyncio 
async def say_hello() :
    print("Hello world !")
    await asyncio.sleep(1)
    print("World")

async def main() :
    loop = asyncio.get_running_loop()
    try : 
        await say_hello()
    finally : 
        loop.stop()        

if __name__ == '__main__' :
    asyncio.run(main())