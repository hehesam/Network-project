import socket
import threading
import subprocess
import os
import tqdm

HEADER = 1024
PORT = 65430
FILE_SIZE = 10

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "DISCONNECT!"
SEPARATOR = "<SEPARATOR>"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(server)

def avg(data_base):
    for st in data_base:
        print(st)
        size = len(st)-2
        res = 0
        for i in range(2,len(st)):
            # print(res, st[i])
            res += int(st[i])
        res = res/size
        st.append(res)

def sort(data_base, sorted_score):
    for st in data_base:
        key = st[-1]
        if key not in sorted_score:
            sorted_score[key] = []
        sorted_score[key].append((st[0],st[1]))
    return sorted(sorted_score.keys())

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    data_base = []
    scores_dict = {}
    while True:
        print("send , avg, sort, max, min,  server, end")
        command = conn.recv(HEADER).decode()
        print("read command : ", command)

        if command == 'send':
            for i in range(FILE_SIZE):
                st_data = conn.recv(HEADER).decode()
                arr = st_data.split("|")
                arr.pop(-1)
                data_base.append(arr)
                print(arr)

        elif command == 'avg':
            avg(data_base)
            print(data_base)
            conn.send("avg has been done !".encode())

        elif command == 'sort':
            sorted_keys = sort(data_base, scores_dict)
            conn.send("sorted avg scorse are : ".encode())
            for avg_score in sorted_keys :
                for id,name in scores_dict[avg_score]:
                    print(id,name)
                    conn.send(id.encode())

        elif command == "max":
            sorted_keys = sort(data_base, scores_dict)
            max_avg_score = sorted_keys[-1]
            id,name = scores_dict[max_avg_score][0]
            conn.send("the name of smart kid is : ".encode())
            conn.send(name.encode())

        elif command == "min":
            sorted_keys = sort(data_base, scores_dict)
            max_avg_score = sorted_keys[0]
            id,name = scores_dict[max_avg_score][0]
            conn.send("the name of smart kid is : ".encode())
            conn.send(name.encode())

        elif command == 'server':
            conn.send(input("tell client: ").encode())

        elif command == 'end':
            print("client disconnected")
            conn.close()
            break
        else:
            print("command is wrong try again")




def start(client_number):

    server.listen()
    for i in range(client_number):
        subprocess.call(["gnome-terminal" , "--" , "sh", "-c", "python3 client.py"])

    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


client_number = int(input("how many client ?"))
start(client_number)