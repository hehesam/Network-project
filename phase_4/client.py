import os.path
import socket
import csv
from student_data import student
HEADER = 1024
PORT = 65430
DISCONNECT_MESSAGE = "DISCONNECT!"
SEPARATOR = "<SEPARATOR>"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_string(msg):
    client.send(msg.encode())

def send_string2(msg):
    st = student()
    client.send(msg.encode())
    st_data = [st.get_ID(), st.get_name(), st.get_score(), st.get_score(), st.get_score(), st.get_score(), st.get_score()]
    for data in st_data:
        print(type(data), data)
        client.send(data.encode())

def send_csv(filename):
    print("write your file")
    st = student()
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(3):
            writer.writerow([st.get_ID(),st.get_name(),st.get_score(), st.get_score(), st.get_score(), st.get_score(),st.get_score()])

    filesize = os.path.getsize(filename)
    client.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}".encode())

    with open(filename, 'rb') as f :
        while True:
            bytes_read = f.read(HEADER)
            # print("bytes_read")
            if not bytes_read:
                print("out of loop")
                break

            client.sendall(bytes_read)
            # client.send(bytes_read)
            print("bytes_read")

    print(filesize)

while True:
    print("0 break 1 for message 2 listing to server")
    command = int(input())
    if command == 1:
        client.send("1".encode())

        while True :
            inp = input("enter your message: ")
            if inp == "break":
                break
            send_string2(inp)

    elif command == 2:
        client.send("2".encode())
        server_message = client.recv(HEADER)
        print(server_message.decode())

    else:
        client.send("0".encode())
        print("byby")
        client.close()
        break