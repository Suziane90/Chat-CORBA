python
from omniORB import CORBA
import ChatApp
import _GlobalIDL, _GlobalIDL__POA

class ChatServerImpl(ChatApp._GlobalIDL.ChatServer, _GlobalIDL__POA.ChatServer):
    def __init__(self):
        self.clients = {}

    def registerClient(self, client):
        print("Client {} connected.".format(client._get_client_id()))
        self.clients[client._get_client_id()] = client
        self.notify_connected_clients()

    def sendMessage(self, sender, message):
        for client in self.clients.values():
            client.receiveMessage(sender, message)

    def getConnectedClients(self):
        return list(self.clients.keys())

    def unregisterClient(self, client_id):
        if client_id in self.clients:
            del self.clients[client_id]
            self.notify_connected_clients()

    def notify_connected_clients(self):
        connected_clients = self.getConnectedClients()
        for client in self.clients.values():
            client.updateConnectedClients(connected_clients)

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