#create a client for the chat application
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5000

s.connect((host, port))

while True:
    response = s.recv(1024)
    decoded_response = str(response, 'utf-8')

    print(decoded_response)

    new_chat_message = input('Send the message: ')
    encoded_chat_message = new_chat_message.encode('utf-8')

    if len(encoded_chat_message) > 0:
        s.send(encoded_chat_message)
