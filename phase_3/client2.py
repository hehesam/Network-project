import socket
HEADER = 1024
PORT = 65430
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
f = open('data.csv', 'rb')

l = f.read(HEADER)
while l :
    print("the type is ",type(l))
    client.send(l)
    l = f.read(HEADER)

f.close()