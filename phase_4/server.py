import socket
import threading
import subprocess
import os
import tqdm

HEADER = 1024
PORT = 65430
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
            print(res, st[i])
            st[i] = int[st[i]]
            res += st[]
        res = res/size
        st.append(res)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    data_base = []

    while True:
        print("send , avg, server")
        command = conn.recv(HEADER).decode()
        print("read command : ", command)

        if command == 'send':
            for i in range(5):
                st_data = conn.recv(HEADER).decode()
                arr = st_data.split("|")
                arr.pop(-1)
                data_base.append(arr)
                print(arr)
            #
            # print("messaging")
            # connected = True
            # while connected:
            #     print("break or get data")
            #     data = conn.recv(HEADER).decode()
            #     print(data)
            #     if data == "break":
            #         print("break: ")
            #         connected = False
            #         break
            #     elif data == "data":
            #         print("data is : ")

        elif command == 'avg':
            print(data_base)
            avg(data_base)
            print(data_base)

        elif command == 'server':
            conn.send(input("tell client: ").encode())

        else:
            print("client disconnected")
            conn.close()
            break





def start(client_number):

    server.listen()
    # for i in range(client_number):
    #     subprocess.call(["gnome-terminal" , "--" , "sh", "-c", "python3 client.py"])

    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        # time.sleep(0.1)
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


start(1)