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
            print(f"Conexão com {websocket.local_address[0]}:{websocket.local_address[1]} fechada.")
            break
        
        print(websocket.local_address)
        print(f"Recebido de {websocket.local_address[0]}:{websocket.local_address[1]}\Requisição recebida: {request}")

        if request['uuid'] == None:
            response = valorant_extractor.fullExtractor(request)
        else:
            response = valorant_extractor.singleExtractor(request)

        await websocket.send(json.dumps(response))

async def main():
    async with websockets.serve(websocket_handler, HOST, PORT):

        print(f"Servidor rodando em http://{HOST}:{PORT}")

        await asyncio.Future()

    

asyncio.run(main())