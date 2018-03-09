import socket
import sys
import random

class Server:

    def __init__(self, no_of_tasks, port_no):
        self.port = port_no
        self.tasks = []
        self.client_task_dictionary = {}
        self.found_clients = False
        for i in range(1, no_of_tasks + 1):
            self.tasks.append(i)

    def launch(self):
        #server socket setup and binding
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', self.port)
        print (sys.stderr, 'starting up on %s port %s' % server_address)
        sock.bind(server_address)

        sock.listen(1)
        
        accepted_first_client = False

        try:
            while(not accepted_first_client):
                connection, client_address = sock.accept()
                print(client_address)
                #message = connection.recv(13).decode('utf-8')
                #if(message == "NEED_NEW_TASK"):
                #    accepted_first_client = True
                accepted_first_client = True

    
            #next_i= random.randint(0,len(self.tasks) - 1)
            #connection.sendall(str(self.tasks[next_i]).encode('utf-8'))
            #self.client_task_dictionary[client_address] = self.tasks[next_i]
        finally:
            connection.close()

        accepted_first_client = False

        try:
            while(not accepted_first_client):
                connection, client_address = sock.accept()
                print(client_address)
                #message = connection.recv(13).decode('utf-8')
                #if(message == "NEED_NEW_TASK"):
                #    accepted_first_client = True
                accepted_first_client = True
    
            #next_i= random.randint(0,len(self.tasks) - 1)
            #connection.sendall(str(self.tasks[next_i]).encode('utf-8'))
            #self.client_task_dictionary[client_address] = self.tasks[next_i]
        finally:
            connection.close()
        #while(not all_clients_have_completed()):
            #print("waiting for a client to accept load")
            #connection, client_address = sock.accept()
            #message = connection.recv(1024).decode('utf-8')
            #is_message_guid = is_guid(message)

            #if(not is_message_guid):
            #    print("Unknown message" + message)
            #    continue

            #client_id = parse_guid(message)
            #if(not self.found_clients):
            #    self.found_clients = True

            #self.client_task_dictionary[client_id] = -1
            #message = connection.recv(1024).decode('utf-8')
            #if(message == "NEED_NEW_TASK"):
            #    try:
            #        print("connection from: ", client_address)
            #        next_i= random.randint(0,len(self.tasks) - 1)
            #        load = self.tasks[next_i]
            #        connection.sendall(str(load).encode('utf-8'))
            #        self.client_task_dictionary[client_id] = load
            #        self.tasks.pop(next_i)
            #    finally:
            #        connection.close()

        #sock.close()

        def all_clients_have_completed():
            all_done = True
            for client in client_task_dictionary:
                if(client_task_dictionary[client]!=-1):
                    all_done = False
                    break
            return all_done

my_server = Server(1,10000)
my_server.launch()