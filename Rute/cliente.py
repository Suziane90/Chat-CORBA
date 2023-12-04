import sys
from omniORB import CORBA
import ChatApp

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
ior = input("Enter the Chat Server's object reference: ")
obj = orb.string_to_object(ior)
chat = obj._narrow(ChatApp.Chat)

if chat is None:
    raise Exception("Object reference is not a Chat")

username = input("Coloque seu nome de usuario: ")
chat.entrarNoChat(username)

while True:
    print("1. Enviar mensaem")
    print("2. Lista de usuarios")
    print("3. Sair do chat")
    choice = input("Escolha uma opção (1/2/3): ")

    if choice == '1':
        message = input("Insira sua mensagem: ")
        chat.sendMessage(username, message)

        received_message = chat.receiveMessage()
        print("Recebida:", received_message)

    elif choice == '2':
        users = chat.listUsers()
        print("Users online:", users)

    elif choice == '3':
        chat.leaveChat(username)
        break

orb.destroy()
