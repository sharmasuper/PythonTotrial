import asyncio
try :
   async def main() :
    print("await before")
    await asyncio.sleep(3)
    print("hello")
    
    print("...world") 

   asyncio.run(main())      
except Exception as e:
  print("show error ",e)