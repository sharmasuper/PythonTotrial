import asyncio 

async def say_hello() :
    print("Hello world")
    await asyncio.sleep(1)
    print("World")

def main() :
    loop = asyncio.get_event_loop()
    try :
        loop.run_until_complete(say_hello())
    finally : 
            #  Close the loop 
            loop.close() 
if __name__ == '__main__' :
    main()            