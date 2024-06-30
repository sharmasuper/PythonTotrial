asyncio.Condition method  
Certainly! The asyncio.Condition class in Python is used to 
wait for some condition to be met. It works similarly to threading
.Condition but is designed for use with asyncio's event loop 
and coroutines.

asyncio.condition class kai method
acquire   , notify
locked , notify_all, locked, release ,wait , wait for


output is
Consumer is waiting for condition.
Producer changed state.value to 1
Consumer received notification: state.value=1

successfully asyncio.Condition method