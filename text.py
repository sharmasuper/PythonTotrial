import asyncio 
# define a coroutine function
async def hello() :
    print("Hello")
    await asyncio.sleep(1)
    print('World')
# Create an event loop

loop = asyncio.get_event_loop()
try:
    # Run a coroutine in the event loop
   
    loop.run_until_complete(hello())

except Exception as e:
        print("show error ",e)

finally : 
    loop.close() 

