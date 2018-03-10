import sys
from server import Server

def server_launch_util(number_of_tasks, port_no):
    my_server = Server(number_of_tasks,port_no)
    my_server.launch()

if __name__ == "__main__":
    try:
        number_of_tasks = sys.argv[1]
        number_of_tasks = int(number_of_tasks)
        if(number_of_tasks<=0):
            raise ValueError
        port_no = sys.argv[2]
        port_no = int(port_no)
        if(port_no<=0):
            raise ValueError
    except:
        print("Invalid arguments. arg1: number of tasks, arg2: port no. Both should have values greater than zero")
        sys.exit()

    server_launch_util(number_of_tasks, port_no)