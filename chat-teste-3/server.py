'Conexão de sala de bate-papo - cliente a cliente'
import threading
import socket
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

# Função para lidar com conexões de clientes

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} saiu do bate-papo!'.encode('utf-8'))
            aliases.remove(alias)
            break
# Função principal para receber a conexão dos clientes

def receive():
    while True:
        print('Servidor rodando e ouvindo ...')
        client, address = server.accept()
        print(f'conexão estabelecida com {str(address)}')
        client.send('apelido?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'O apelido desse cliente é {alias}'.encode('utf-8'))
        broadcast(f'{alias} está conectado neste bate-papo'.encode('utf-8'))
        client.send('agora você está conectado!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
