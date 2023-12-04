from omniORB import CORBA
import ChatApp__POA

class ChatServant(ChatApp__POA.Chat):
    
    def __init__(self):
        self.usuario = []
        self.messages = []

    def sendMessage(self, username, message):
        formatted_message = f"{username}: {message}"
        print(formatted_message)
        self.messages.append(formatted_message)

    def receiveMessage(self):
        if self.messages:
            return self.messages.pop(0)
        else:
            return "Sem mensagens"

    def entrarNoChat(self, username):
        self.usuario.append(username)
        print(f"{username} entrou no chat.")

    def leaveChat(self, username):
        self.usuario.remove(username)
        print(f"{username} saiu do chat.")

    def listUsers(self):
        return ', '.join(self.usuario)

orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

chatServant = ChatServant()
chatObject = chatServant._this()

print("Servidor do Chat rodando...")
print("Objeto de referencia:", orb.object_to_string(chatObject))

orb.run()
