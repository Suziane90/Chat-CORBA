import sys
from omniORB import CORBA, PortableServer
import ChatApp, ChatApp__POA

class ChatServant(ChatApp__POA.ChatServer):
    def __init__(self):
        self.clients = {}

    def registerClient(self, username, client):
        self.clients[username] = client

    def unregisterClient(self, username):
        if username in self.clients:
            del self.clients[username]

    def broadcastMessage(self, message):
        for client in self.clients.values():
            client.receiveMessage(message)

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

chatServant = ChatServant()
chatObj = chatServant._this()

print("Chat Server ready...")
orb.run()
