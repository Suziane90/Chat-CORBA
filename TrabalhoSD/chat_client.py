from omniORB import CORBA
from chat import ChatApp
import sys

try:
    orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
    ior = sys.argv[1]
    obj = orb.string_to_object(ior)

    chat = obj._narrow(ChatApp.Chat)
    if chat is None:
        print("Object reference is not a Chat")
        sys.exit(1)

    while True:
        message = input("Enter your message (type 'exit' to quit): ")

        if message.lower() == 'exit':
            break

        chat.sendMessage(message, "Client")
        received_message = chat.receiveMessage()
        print(f"Received message: {received_message}")

except CORBA.Exception as ex:
    print(f"CORBA Exception: {ex}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    orb.destroy()
