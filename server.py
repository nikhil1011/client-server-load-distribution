import socket
import sys
import random
from uuid import UUID
class Server:

    def __init__(self, no_of_tasks, port_no):
        self.port = port_no
        self.tasks = []
        self.client_task_dictionary = {}
        self.found_clients = False
        self.client_list = []
        for i in range(1, no_of_tasks + 1):
            self.tasks.append(i)

    def parse_guid(self, guid_string, version = 4):
        try:
            uuid_obj = UUID(guid_string, version=version)
            return uuid_obj
        except:
            return False

    def all_clients_are_free(self):
        all_clients_free = True
        for client in self.client_task_dictionary:
            if(self.client_task_dictionary[client] != -1):
                all_clients_free = False
                break
        return all_clients_free

    def launch(self):
        #server socket setup and binding
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', self.port)
        print ('starting up on %s port %s' % server_address)
        sock.bind(server_address)

        sock.listen(1)
        
        first_client_accepted = False

        while(not first_client_accepted):
            connection, client_id = sock.accept()
            guid_message = connection.recv(36).decode('utf-8')
            print("received guid_message:", guid_message)
            guid = self.parse_guid(guid_message, 4)
            if(not guid):
                connection.close()
                continue
            message = connection.recv(13).decode('utf-8')
            if(message == "NEED_NEW_TASK"):
                first_client_accepted = True
                print("Sending task type -1 from first loop")
                connection.sendall(str(-1).encode('utf-8'))
                next_i= random.randint(0,len(self.tasks) - 1)
                load = self.tasks[next_i]
                print("Sending task ", load,"from first loop")
                connection.sendall(str(load).encode('utf-8'))
                self.client_task_dictionary[guid] = load
                self.tasks.pop(next_i)

            connection.close()

        while(len(self.tasks)>0):
            connection, client_id = sock.accept()
            guid_message = connection.recv(36).decode('utf-8')
            print("received guid_message:", guid_message)
            guid = self.parse_guid(guid_message)
            if(not guid):
                connection.close()
                continue
            message = connection.recv(13).decode('utf-8')
            if(message == "NEED_NEW_TASK"):
                print("Sending task type -1 from second loop")
                connection.sendall(str(-1).encode('utf-8'))

                next_i= random.randint(0,len(self.tasks) - 1)
                load = self.tasks[next_i]
                print("Sending task ", load, "from second loop")
                connection.sendall(str(load).encode('utf-8'))
                self.client_task_dictionary[guid] = load
                self.tasks.pop(next_i)
            connection.close()

        while(not self.all_clients_are_free()):
            connection, client_id = sock.accept()
            guid_message = connection.recv(36).decode('utf-8')
            print("received guid_message:", guid_message)
            guid = self.parse_guid(guid_message)
            if(not guid):
                connection.close()
                continue
            message = connection.recv(13).decode('utf-8')
            if(message == "NEED_NEW_TASK"):
                print("Sending SHUT_DOWN (task 2) signal")
                connection.sendall(str(-2).encode('utf-8'))
                self.client_task_dictionary[guid] = -1
                print("Sending SHUT DOWN signal")
                connection.sendall("SHUT_DOWN".encode('utf-8'))
            connection.close()

        print("Completed all tasks using: ",len(self.client_task_dictionary)," clients")
        print("Shutting down server...")
        sock.close()


my_server = Server(10,10000)
my_server.launch()