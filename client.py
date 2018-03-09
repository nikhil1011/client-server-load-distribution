import socket
import sys
import random
import uuid
import time
from threading import Thread

class Client:
    def __init__(self, port_no):
        self.server_port = port_no
        self.client_id = uuid.uuid4()
    
    def is_number(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def perform_task(self, string):
        task_status = ""

        if(not self.is_number(string)):
            task_status = "Could not parse instruction:" + string
        else:
            load = int(string)
            print("Performing task ", load, " will take ", load, "seconds to complete")
            try:
                time.sleep(load)
                task_status = "Completed task"
            except:
                task_status = "Could not complete task, there was an exception."

        return task_status

    def connect(self):

        print("Starting client:", self.client_id)
        # Create a TCP/IP socket
        

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', self.server_port)
        print('connecting to %s port %s' % server_address)
        #try:
        #    sock.connect(server_address)
        #except:
        #    print("Could not connect to server. Shutting down client.")
        #    return
        #sock.close()
        while(True):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(server_address)
            except:
                print("Could not connect to server. Shutting down client.")
                sock.close()
                return
            try:
                sock.sendall(str(self.client_id).encode('utf-8'))
                sock.sendall("NEED_NEW_TASK".encode('utf-8'))

                instruction_type = sock.recv(2).decode('utf-8')
                if(len(instruction_type) == 0):
                    xda = 1
                instruction_type = int(instruction_type)
                if(instruction_type == -1):
                    instruction = sock.recv(20).decode('utf-8')
                    print("Received instruction: ", instruction)
                    task_status = self.perform_task(instruction)
                    print("Task Status:", task_status,", Instruction: ", instruction)
                if(instruction_type == -2):
                    instruction = sock.recv(9).decode('utf-8')
                    print("Received instruction: ", instruction)
                    break

            finally:
                sock.close()

        print("Shutting down Client", self.client_id)
        #task = sock.recv(1024).decode('utf-8')
        #print(task)

        #sock.sendall("NEED_NEW_TASK".encode('utf-8'))
        #message = sock.recv(1024).decode('utf-8')

        #print("received:",message)
        #print("shutting down")

        sock.close()

#my_client = Client(10000)
#my_client2 = Client(10000)
#Thread(target = my_client.connect()).start()
#Thread(target = my_client2.connect()).start()