#create a server for a chat application
import socket
import sys

def create_chat_socket():
    try:
        global host
        global port
        global s

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 5000

    except socket.error as err:
        print(f"Socket cannot be created {err}")

def bind_chat_socket():
    try:
        global host
        global port
        global s

        s.bind((host, port))
        s.listen((4))

        print(f"Connection established on {port}")

    except socket.error as err:
        print(f'Cannot bind on {port}')

def accept_chat_socket():
    global s
    try:
        cli_socket, addr = s.accept()
        send_chat(cli_socket)
        print(f'Connected to {addr}')
        cli_socket.close()

    except socket.error as err:
        print(f"Cannot connect to the client")

def send_message(cli_socket):
    global s
    while True:
        try:
            chat_message = input("Send message: ")
            encoded_chat_message = bytes(chat_message, 'utf-8')
            if 'bye' in chat_message:
                cli_socket.close()
                s.close()
                sys.exit()

            if len(encoded_chat_message) > 0:
                reply = cli_socket.recv(1024)
                decoded_reply = reply.decode('utf-8')

                print(decoded_reply)

        except socket.error as err:
            print(f"Error in sending the message: {err}")

if __name__ == '__main__':
    create_chat_socket()
    bind_chat_socket()
    accept_chat_socket()
