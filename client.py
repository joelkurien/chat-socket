#create a client for the chat application
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5000

s.connect((host, port))

userName = input("Name: ")
encoded_userName = bytes(userName, 'utf-8')

if len(encoded_userName) > 0:
    s.send(encoded_userName)

    while True:
        new_chat_message = input(f'{userName}: ')
        encoded_chat_message = new_chat_message.encode('utf-8')

        if len(encoded_chat_message) > 0:
            s.send(encoded_chat_message)
