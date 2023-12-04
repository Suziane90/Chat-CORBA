import sys
from omniORB import CORBA, PortableServer
import ChatApp, ChatApp__POA

try:
    orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
    ior = input("Digite o IOR do servidor: ")

    obj = orb.string_to_object(ior)
    chat = obj._narrow(ChatApp.ChatServer)

    if chat is None:
        print("Referência de objeto não é um ChatServer")
        sys.exit(1)

    username = input("Digite seu nome de usuário: ")
    chatClient = ChatApp.ChatClient_i()

    # Registra o cliente no servidor
    chat.registerClient(username, chatClient)

    print(f"Bem-vindo ao chat, {username}!")

    while True:
        message = input("Digite sua mensagem (digite 'exit' para sair): ")

        if message.lower() == 'exit':
            break

        # Envia a mensagem para o servidor
        chat.sendMessage(username, message)

except CORBA.Exception as ex:
    print(f"Exceção CORBA: {ex}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    # Remove o cliente quando ele sai
    chat.unregisterClient(username)
    orb.destroy()
