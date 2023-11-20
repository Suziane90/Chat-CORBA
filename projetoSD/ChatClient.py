from omniORB import CORBA
import Chat
import sys

# Inicialize o ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Obtenha a referência do objeto do serviço de nomes
obj = orb.resolve_initial_references("NameService")._narrow(CORBA.CORBA_Object)

if obj is None:
    print("Erro: Não foi possível obter a referência do objeto.")
    sys.exit(1)

# Estreite a referência do objeto para a interface de chat
chat_obj = obj.resolve_initial_references("ChatServer")._narrow(Chat.ChatServer)

if chat_obj is None:
    print("Erro: Referência do objeto de chat inválida.")
    sys.exit(1)

# Interaja com o servidor de chat
username = input("Digite seu nome de usuário: ")

while True:
    message = input("Digite uma mensagem (ou 'exit' para sair): ")
    if message.lower() == 'exit':
        break
    chat_obj.sendMessage(username, message)
    received_message = chat_obj.receiveMessage(username)
    if received_message:
        print(f"Received message: {received_message}")

# Encerre o ORB
orb.shutdown(True)
