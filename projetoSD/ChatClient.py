from omniORB import CORBA
import Chat
import sys

# Inicialize o ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Obtenha o IOR do servidor do outro computador
server_ior = input("Digite o IOR do servidor: ")

# Estreite a referência do objeto para a interface de chat
obj = orb.string_to_object(server_ior)
chat_obj = obj._narrow(Chat.ChatServer)

if chat_obj is None:
    print("Erro: Referência do objeto inválida.")
    sys.exit(1)

# Interaja com o servidor de chat
while True:
    message = input("Digite uma mensagem (ou 'exit' para sair): ")
    if message.lower() == 'exit':
        break
    chat_obj.sendMessage(message)
    received_message = chat_obj.receiveMessage()
    print(f"Received message from server: {received_message}")

# Encerre o ORB
orb.shutdown(True)
