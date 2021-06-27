#create a server for a chat application
import socket
import sys

class Chat_Server:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = 5000

        self.bind_chat_socket()
        self.accept_chat_socket()

    def bind_chat_socket(self):
        try:
            self.s.bind((self.host, self.port))
            self.s.listen((4))

            print(f"Connection established on {self.port}")

        except socket.error as err:
            print(f'Cannot bind on {self.port}')

    def send_chat(self, cli_socket):
        while True:
            chat_message = input("Send message: ")
            encoded_chat_message = bytes(chat_message, 'utf-8')
            if len(encoded_chat_message) > 0:
                cli_socket.send(encoded_chat_message)

                reply = cli_socket.recv(1024)
                decoded_reply = str(reply, 'utf-8')
                if 'bye' in decoded_reply:
                    cli_socket.close()
                    self.s.close()
                    sys.exit()

                print(decoded_reply)

    def accept_chat_socket(self):
        try:
            cli_socket, addr = self.s.accept()
            self.send_chat(cli_socket)
            print(f'Connected to {addr}')
            cli_socket.close()

        except socket.error as err:
            print(f"Cannot connect to the client")


if __name__ == '__main__':
    chat = Chat_Server()
