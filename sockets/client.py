import asyncio
from websockets.sync.client import connect

def client():
    with connect("ws://127.0.0.1:8080") as websocket:
        while True:
            send = input('Mande algo (ou deixe vazio para sair): ')

            if not send:
                websocket.close()
                break
        
            websocket.send(send)

            message = websocket.recv()

            print(f"Received: {message}")

client()