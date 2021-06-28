#create a server for a chat application
import socket
import sys

class ChatServer:
    allConnections = []
    __allAddresses = [] #just for the developer
    allNames = []

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
            if cli_socket == self.s:
                print('Hello')
            reply = cli_socket.recv(1024)
            decoded_reply = str(reply, 'utf-8')
            if 'bye' in decoded_reply:
                cli_socket.close()
                self.s.close()
                sys.exit()

            print(decoded_reply)

    #Connecting all the clients to the server
    def accept_chat_socket(self):
        try:
            cli_socket, addr = self.s.accept()
            self.allConnections.append(cli_socket)
            self.__allAddresses.append(addr)

            usrName = cli_socket.recv(1024)
            decoded_usrName = str(usrName, 'utf-8')
            self.allNames.append(decoded_usrName)

            self.send_chat(cli_socket)
            print(f'Connected to {addr}')
            cli_socket.close()

        except socket.error as err:
            print(f"Cannot connect to the client")

if __name__ == '__main__':
    chat = ChatServer()
