import socket
HEADER = 1024
PORT = 65430
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"[LISTENING] Server2 is listening on {SERVER}")

conn, addr = server.accept()
f = open("server_file.csv", 'wb')

l = conn.recv(HEADER)
while l:
    f.write(l)
    l = conn.recv(HEADER)

f.close()
conn.close()