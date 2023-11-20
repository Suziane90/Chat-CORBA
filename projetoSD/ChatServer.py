from omniORB import CORBA
import Chat
import sys

class ChatServer_i(Chat.ChatServer):
    def __init__(self):
        self.messages = []

    def sendMessage(self, message):
        print(f"Received message: {message}")
        self.messages.append(message)

    def receiveMessage(self):
        if self.messages:
            return self.messages.pop(0)
        else:
            return ""

# Inicialize o ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Crie uma instância do servidor de chat
Chat_Server = ChatServer_i()

# Obtém a referência do objeto
obj = orb.resolve_initial_references("RootPOA")._get_the_POAManager()
poa_manager = obj.activate()
poa = orb.resolve_initial_references("RootPOA")

# Ative o servidor de chat
poaManager = poa._get_the_POAManager()
poaManager.activate()
poa.servant_to_reference(Chat_Server)

# Aguarde chamadas de clientes
orb.run()


# Imprima o IOR
ior = orb.object_to_string(Chat_Server._this())
print("IOR do servidor:", ior)
