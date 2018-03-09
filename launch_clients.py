import sys
import os
from client import Client
from multiprocessing import Process

if __name__ == "__main__":
    number_of_clients = 0
    try:
        number_of_clients = "2"
        number_of_clients = int(number_of_clients)
        if(number_of_clients<=0):
            raise ValueError
    except:
        print("Invalid arguments. Enter a number greater than zero.")
        sys.exit()

    #for i in range(number_of_clients):
    #    os.system("python spawn_client.py")

    client1 = Client(10000)
    client2 = Client(10000)

    p1 = Process(target = client1.connect())
    p2 = Process(target = client2.connect())