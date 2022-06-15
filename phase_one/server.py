import socket
import threading
import subprocess
import time
HEADER = 64
PORT = 65432
# SERVER =  "172.17.40.1" 
# or 
SERVER = socket.gethostbyname(socket.gethostname())
# print("ip is : ",SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)



def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")


    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length :

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))  #to send message from server to client
    conn.close()



def start(client_number):
    server.listen()

    print(f"[LISTENING] Server is listening on {SERVER}")
    # for j in range(client_number):
    #     subprocess.call('start python client.py', shell=True)

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        # time.sleep(0.1)
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARING] sever is starting...")
client_number = int(input("how many client ?"))
start(client_number)
