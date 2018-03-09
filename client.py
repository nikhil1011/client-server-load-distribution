import socket
import sys
import random

class Client:
    def __init__(self, port_no):
        self.server_port = port_no

    def connect(self):

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', self.server_port)
        print('connecting to %s port %s' % server_address)
        sock.connect(server_address)
        sock.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)

        message = "This is a message."
            # Look for the response
        amount_received = 0
        amount_expected = len(message.encode('utf-8'))
    
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received "%s"' % data.decode('utf-8'))

#my_server = server.Server(1,10000)
#my_server.launch()
my_client = Client(10000)
my_client.connect()