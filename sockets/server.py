import asyncio
import websockets
import json

from extractor import genius_extractor

HOST = '127.0.0.1'
PORT = 8080

async def websocket_handler(websocket):
    while True:
        try: 
            request = await websocket.recv()
        except websockets.ConnectionClosedOK:
            print(f"Conexão com {websocket.local_address[0]}:{websocket.local_address[1]} fechada.")
            break
        
        print(websocket.local_address)
        print(f"Recebido de {websocket.local_address[0]}:{websocket.local_address[1]}\Requisição recebida: {request}")

        response = genius_extractor.extractor(json.loads(request))

        await websocket.send(response)



async def main():
    async with websockets.serve(websocket_handler, HOST, PORT, ):

        print(f"Servidor rodando em http://{HOST}:{PORT}")

        await asyncio.Future()

    

asyncio.run(main())