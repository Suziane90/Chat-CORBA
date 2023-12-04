python
from omniORB import CORBA
import ChatApp
import _GlobalIDL, _GlobalIDL__POA
from threading import Thread

class ChatClientImpl(ChatApp._GlobalIDL.ChatClient, _GlobalIDL__POA.ChatClient):
    def __init__(self, client_id, server):
        self.client_id = client_id
        self.server = server

    def _get_client_id(self):
        return self.client_id

    def receiveMessage(self, sender, message):
        print("[{}]: {}".format(sender, message))

    def updateConnectedClients(self, connected_clients):
        print("Connected clients: {}".format(connected_clients))

def run_client(server, client_id):
    orb = CORBA.ORB_init()

    # Inicializando o servidor CORBA
    poa = orb.resolve_initial_references("RootPOA")
    poaManager = poa._get_the_POAManager()
    poaManager.activate()

    # Criando uma instância do ChatClient
    client = ChatClientImpl(client_id, server)

    # Obtendo uma referência CORBA para o cliente
    client_ref = client._this()

    # Registrando o cliente no servidor
    server.registerClient(client)

    # Inicializando o ORB para esperar por invocações
    orb.run()

if __name__ == "__main__":
    orb = CORBA.ORB_init()

    # Inicializando o servidor CORBA
    poa = orb.resolve_initial_references("RootPOA")
    poaManager = poa._get_the_POAManager()
    poaManager.activate()

    # Criando uma instância do ChatServer
    server = ChatServerImpl()

    # Obtendo uma referência CORBA para o servidor
    server_ref = server._this()

    # Inicializando o ORB para esperar por invocações
    orb.run()

    # Inicializando o servidor em uma thread separada
    server_thread = Thread(target=server.run)
    server_thread.start()

    # Inicializando vários clientes em threads separadas
    for i in range(3):
        client_thread = Thread(target=run_client, args=(server, "Client{}".format(i)))
        client_thread.start()