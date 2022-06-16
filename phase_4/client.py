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

def send_string2():
    st = student()
    for i in range(5):
        res = ""
        st_data = [st.get_ID(), st.get_name(), st.get_score(), st.get_score(), st.get_score(), st.get_score(), st.get_score()]
        for data in st_data:
            res += data + "|"
        client.send(res.encode())
        print(res)

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
    print("end  send  server avg")
    command = input()
    if command == "send":
        client.send("send".encode())
        send_string2()

    elif command == "avg":
        client.send("avg".encode())

    elif command == "sort":
        client.send("sort".encode())
        for i in range(5):
            sort_id = client.recv(HEADER)
            print(sort_id.decode())


    elif command == "server":
        client.send("2".encode())
        server_message = client.recv(HEADER)
        print(server_message.decode())

    elif command == "end":
        client.send(DISCONNECT_MESSAGE.encode())
        print("byby")
        client.close()
        break