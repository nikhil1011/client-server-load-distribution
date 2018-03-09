import sys
from server import Server
def server_launch_util(number_of_tasks):

    my_server = Server(number_of_tasks,10000)
    my_server.launch()

if __name__ == "__main__":
    try:
        number_of_tasks = sys.argv[1]
        number_of_tasks = int(number_of_tasks)
        if(number_of_tasks<=0):
            raise ValueError
    except:
        print("Invalid arguments. Enter a number greater than zero.")
        sys.exit()

    server_launch_util(number_of_tasks)