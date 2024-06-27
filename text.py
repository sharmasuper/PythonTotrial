import asyncio
import os
import signal

async def main():
    # Subprocess शुरू करें
    process = await asyncio.create_subprocess_exec(
        'sleep', '10',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    pid = process.pid

    def child_handler():
        print(f"Child process {pid} changed state")

    # सिग्नल हैंडलर सेट करें
    loop = asyncio.get_event_loop()
    loop.add_child_handler(pid, child_handler)

    # कुछ समय के लिए इंतजार करें
    await asyncio.sleep(2)

    # सिग्नल हैंडलर हटाएं
    loop.remove_child_handler(pid)
    print(f"Child handler for process {pid} removed")

    # Subprocess को समाप्त करने की प्रतीक्षा करें
    await process.wait()

asyncio.run(main())
