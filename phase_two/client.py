import socket

HEADER = 1024
PORT = 65431
DISCONNECT_MESSAGE = "DISCONNECT!"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    # message = msg.encode()
    # msg_length = len(message)
    # send_length = str(msg_length).encode()
    client.send(msg.encode())

    server_message = client.recv(HEADER)
    print(server_message.decode())


print("type something")
while True:
    inp = input()
    if inp == "break":
        break
    send(inp)
send(DISCONNECT_MESSAGE)
