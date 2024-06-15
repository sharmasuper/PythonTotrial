# function Caching - jab ek function ek hu value ai liy kahi bar call hota ---
import functools
import time
@functools.lru_cache(maxsize=None)

def fx(n) :
    time.sleep(1)
    return n*5


print(fx(20))
print("done for 20")    

print(fx(2))
print("done for 20")    

print(fx(6))
print("done for 20") 
print("second call memoize function")   


print(fx(20))
print("done for 20")    

print(fx(2))
print("done for 20")    

print(fx(6))
print("done for 20") 

