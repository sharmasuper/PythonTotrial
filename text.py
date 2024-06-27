# set_event_loop(loop) method example in python in asyncio
# The set_event_loop(loop) method in asyncio is used to set a specific event loop instance as the current event loop. This can be useful when you want to manage or switch between different event loops programmatically. Here’s an example that demonstrates the usage of set_event_loop(loop):



import asyncio

async def countdown() :
    for i in range(5,0,-1) :
        print(f"countdown : {i}")
        await asyncio.sleep(1)

loop1 = asyncio.new_event_loop()
loop2 = asyncio.new_event_loop()

# Run coroutine in loop1
async def run_coroutine_in_loop1() :
    asyncio.set_event_loop(loop1)
    print("Running coroutine in loop1")
    await countdown()

async def run_coroutine_in_loop2() :
    asyncio.set_event_loop(loop2)
    print("Runnig coroutine in loop2")
    await countdown()


async def main() :
    print("Starting countdown in loop1")
    await run_coroutine_in_loop1()

    print("\n Starting countdown in loop2 ")
    await run_coroutine_in_loop2()


if __name__ == '__main__':
    asyncio.run(main()) 



   