'Conexão de sala de bate-papo - cliente a cliente'
import threading
import socket
host = '0.0.0.0'  # Usei esse para ser acessivel em qualquer lugar, ou endereço da maquina onde o servidor ira rodar
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
            broadcast(f'{alias} \n saiu do bate-papo!\n '.encode('utf-8'))
            aliases.remove(alias)
            break
# Função principal para receber a conexão dos clientes

def receive():
    print(f'Servidor rodando e ouvindo em {host}:{port} ...')
    while True:
        client, address = server.accept()
        print(f'Conexão estabelecida com {str(address)}')
        alias = client.recv(1024).decode('utf-8')
        aliases.append(alias)
        clients.append(client)
        print(f'O apelido deste cliente é {alias}')
        broadcast(f'{alias} está conectado neste chat'.encode('utf-8'))
        client.send('Agora você está conectado!\n'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
