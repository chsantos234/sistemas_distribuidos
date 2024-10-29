import asyncio
import websockets
import json

from extractor import valorant_extractor

HOST = '127.0.0.1'
PORT = 8080

async def websocket_handler(websocket):
    while True:
        try: 
            request = await websocket.recv()
            request = json.loads(request)
        except websockets.ConnectionClosedOK:
            print(f"CONEXÃO COM {websocket.local_address[0]}:{websocket.local_address[1]} FECHADA.\n")
            print("-*"*30, '\n')
            break
        
        print(f"RECEBIDO DE {websocket.local_address[0]}:{websocket.local_address[1]}: {request} \n")

        if request['type'] == "chat":
            response = valorant_extractor.getGPTRequest(request)
        elif request['uuid'] == None:
            response = valorant_extractor.fullExtractor(request)
        else:
            response = valorant_extractor.singleExtractor(request)

        await websocket.send(json.dumps(response))
        print(f"RESPOSTA ENVIADA PARA: {websocket.local_address[0]}:{websocket.local_address[1]}\n")

async def main():
    async with websockets.serve(websocket_handler, HOST, PORT):

        print(f"\nSERVIDOR RODANDO EM: http://{HOST}:{PORT} \n")

        await asyncio.Future()

    

asyncio.run(main())