asyncio.DatagramProtocol
method => 1 datagram_received   2 error_recived

import asyncio
class EchoClientProtocol(asyncio.DatagramProtocol) :
    def __init__(self,message,loop) :
        self.message = message
        self.loop = loop 

    def connection_made(self,tranport) :
        self.tranport = tranport 
        print("f senfing message :",self.message)
        self.tranport.sendto(self.message.encode())

    def datagram_received(self,data,addr) :
        message = data.encode()
        # data.encode() per nahi chal raha h yai
        print(f"Recived {message} from {addr}")
        print("Closing tranport")
        self.tranport.close()
    def connection_lost(self,exc) :
        print("Conneciton closed")
        self.loop.stop()


async def main() :
    loop = asyncio.get_running_loop()
    message = "Hello,World !"
    protocol = EchoClientProtocol(message,loop)
    transport,ALLcallingFunction  = await loop.create_datagram_endpoint(
        lambda : protocol,
        remote_addr = ('127.0.0.1',9999)
    )
    ALLcallingFunction.connection_made(transport)
    ALLcallingFunction.datagram_received("Hello,this is a test",('127.0.0.1'))
    # ALLcallingFunction.connection_lost()
 #transport,_ this _ method issai hum any function call kar sktai h

    try : 
      await asyncio.sleep(2)
    finally : 
            transport.close()
asyncio.run(main())   #//output is f senfing message : Hello,World !
#Conneciton closed     


              



