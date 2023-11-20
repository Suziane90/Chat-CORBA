from omniORB import CORBA
import CosNaming
import Chat

class ChatServer_i(Chat.ChatServer):
	def__init__(self):
		self.messages = []
	
	def sendMessage(self, user, message):
		self.messages.append(f"{user}: {message}")
		return "Mensagem mandada com sucesso!"
		
	def getMessages(self):
		return "\n".join(self.messages)

# Inicializar o ORB
orb = CORBA.ORB_init()

# Obter referência para o root POA
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()

# Criar uma instância do servidor
chatServer = ChatServer_i

# Ativar o servidor
poaManager.activate()

# Obter referência para o objeto do servidor
obj = chatServer._this

# Obter referência para o serviço de nomes
nameService = orb.resolve_initial_references("NameService")
rootContext = nameService.narrow(CosNaming.NamingContext)

# Registrar o objeto no serviço de nomes
name = [CosNaming.NameComponent("ChatServer", "")]
rootContext.rebind(name, obj)

# Aguardar chamadas
obr.run()
