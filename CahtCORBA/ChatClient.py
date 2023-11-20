from omniORB import CORBA
import CosNaming
import Chat

orb = CORBA.ORB_init()

# Obter referência para o serviço de nomes
nameService = orb.resolve_initial_references("NameService")
rootContext = nameService.narrow(CosNaming.NamingContext)

# Obter referência para o objeto do servidor
name = [CosNaming.NameComponent("ChatServer", "")]
obj = rootContext.resolve(name)

# Conectar ao objeto do servidor
user = "Luan"
message = "Olá. como vai?"

response = chatServer.sendMessage(user, message)
print(response)

messages = chatServer.getMessages()
print(f"Mensagens:\n{messages}")
