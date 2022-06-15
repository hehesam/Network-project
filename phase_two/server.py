import socket
import threading
import subprocess

HEADER = 1024
PORT = 65431
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "DISCONNECT!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(server)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        data = conn.recv(HEADER).decode()
        if data == DISCONNECT_MESSAGE:
            break
        print(data)
        conn.send(str.encode("hello client"))
    conn.close()

def start():
    server.listen()
    # subprocess.call(["gnome-terminal" , "--" , "sh", "-c", "python3 client.py"])
    # subprocess.call(["gnome-terminal" , "--" , "sh", "-c", "python3 client.py"])

    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        # time.sleep(0.1)
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


start()