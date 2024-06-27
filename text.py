import asyncio 

async def Hello():
  print("Hello start")
  await asyncio.sleep(1) 
  print('World')

async def main() :
    loop = asyncio.get_event_loop()
    print("current evnet loop ",loop)
    await Hello()

if __name__ =="__main__" :
    asyncio.run(main())    
 
