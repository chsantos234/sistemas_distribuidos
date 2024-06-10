import socket

# criação de um objeto socket
# AF_INET - Address Family  IPv4
# AF_INET6 - Address Family IPv6
# SOCK_STREAM - TCP
# SOCK_DGRAM - UDP

HOST = "127.0.0.1" # ip do servidor (localhost)
PORT = 8080 # porta do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        send = input('Mande algo (ou deixe vazio para sair): ')

        if not send:
            break  # Sai do loop se send for vazia

        # envia informação ao servidor
        s.sendall(bytes(f"{send}", "utf-8"))

        # recebe informação do servidor
        data = s.recv(4096)
        print(f"Recebido {data.decode('utf-8')}")

print("Conexão fechada.")