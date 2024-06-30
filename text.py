#In Python, asyncio.CancelledError is an exception that is raised when an asyncio.Task is cancelled. Here's a simple example to illustrate how it works:

import asyncio 

async def some_task() :
    try :
        print("Task started")
        await asyncio.sleep(5)
    except asyncio.CancelledError : 
        print("Task was cancelled")  
        raise  # Re-raise the exception to let the task know it was cancelled

async def main() :
    task = asyncio.create_task(some_task())
    # let the task run for a bit
    await asyncio.sleep(5)
    # Cancel the task
    task.cancel()
    try :
        await task
    except asyncio.CancelledError :
        print("Handeed cancellaintion in main")     
asyncio.run(main())