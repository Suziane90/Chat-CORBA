from omniORB import CORBA
import Chat
import sys

class ChatServer_i(Chat.ChatServer):
    def __init__(self):
        self.messages = {}

    def sendMessage(self, username, message):
        if username not in self.messages:
            self.messages[username] = []
        self.messages[username].append(message)

    def receiveMessage(self, username):
        if username in self.messages:
            if self.messages[username]:
                return self.messages[username].pop(0)
        return ""

# Inicialize o ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Crie uma instância do servidor de chat
chat_server = ChatServer_i()

# Obtém a referência do objeto
obj = orb.resolve_initial_references("RootPOA")._get_the_POAManager()
obj.activate()

# Registre o servidor no serviço de nomes
chat_obj = chat_server._this()

# Aguarde chamadas de clientes
orb.run()

