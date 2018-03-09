from client import Client

if __name__ == "__main__":
    my_client = Client(10000)
    my_client.connect()
    input("Press any key for exit")