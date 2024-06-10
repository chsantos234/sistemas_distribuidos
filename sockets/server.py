import socket
import threading

HOST = '127.0.0.1' # localhost
PORT = 8080 # porta
MAX_CLIENTS = 5 # número máximo de clientes em paralelo (threads)

def handle_client(client_socket, client_address):
    """
    Trata uma nova conexão com um cliente recebido.
    Recebe e responde mensagens recebidas.
    """
    print(f"Conexão recebida de {client_address[0]}:{client_address[1]}")
    
    while True:
        #try:
        data = client_socket.recv(8192).decode('utf-8')
        if not data:
            break # Sai do loop se data for vazia
        
        print(f"Recebido de {client_address[0]}:{client_address[1]}:\n{data}")

        response = f"Servidor recebeu isso: {data}"

        client_socket.send(response.encode('utf-8'))
        #except ConnectionResetError:
            #print(f"A conexão com {client_address[0]}:{client_address[1]} foi encerrada pelo cliente.")
            #break

    print(f"Conexão com {client_address[0]}:{client_address[1]} fechada.")
    client_socket.close()

def main():
    """
    Inicia o socket do servidor com TCP e conexões com sockets clientes
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    # max connection queue
    s.listen(MAX_CLIENTS)

    print(f"Servidor rodando em http://{HOST}:{PORT}")

    while True:
        client_socket, client_address = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()