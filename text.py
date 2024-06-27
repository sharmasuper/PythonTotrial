import asyncio 
import os
import signal


async def child_task() :
    print(f"child process {os.getpid()} started")
    await asyncio.sleep(1) 
    print(f"child process {os.getpid} exiting")
    os.exit(0)


def child_handler(pid,returncode,*args):
    print(f"child process {pid} exited with return code {returncode}")
    print(f"Additional argunment : {args}")

async def main() :
    loop = asyncio.get_running_loop()
    # watcher = asyncio.ThreadedChildWatcher()
    # watcher.attach_loop(loop)
    # loop.set_child_watcher(watcher)

    # Start a child process

    watcher = asyncio.ThreadedChildWatcher()
    watcher.attach_loop(loop) 
    loop.set_child_watcher(watcher)
    # start a child process
    
    pid = os.fork()
    print(pid)
    if pid == 0 :
        # this is child process
        await child_task()

    else :
        # this is the parent prcess 
        print(f"Parent process {os.getpid()} with child PID {pid}")
        # Add the child handler
        watcher.add_child_handler(pid,child_handler,"arg1","arg2")
        # Keep the event loop runnig to handle the child process
        
        try :
            await asyncio.sleep(10)
        except asyncio.CancelledError:
            pass 

if __name__ == '__main__' :
    asyncio.run(main())         
























