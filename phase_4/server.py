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

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        command = conn.recv(HEADER).decode()


        if command == '1':
            print("messaging")
            connected = True
            while connected:
                data = conn.recv(HEADER).decode()
                print(data)

                if data == DISCONNECT_MESSAGE:
                    break
                if data == "data":
                    for i in range(7):
                        st_data = conn.recv(HEADER).decode()
                        print(st_data)

        elif command == '2':
            conn.send(input("tell client: ").encode())

        elif command == '0':
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