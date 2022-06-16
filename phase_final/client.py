import os.path
import socket
import csv
from student_data import student
HEADER = 1024
PORT = 65430
FILE_SIZE = 10
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
    for i in range(FILE_SIZE):
        res = ""
        st_data = [st.get_ID(), st.get_name(), st.get_score(), st.get_score(), st.get_score(), st.get_score(), st.get_score()]
        for data in st_data:
            res += data + "|"
        client.send(res.encode())
        print(res)

def send_csv(filename):
    print("write your file")
    client.send(filename.encode())
    st = student()
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID','name','score1','score2','score3','score4','score5'])
        for i in range(FILE_SIZE):
            writer.writerow([st.get_ID(),st.get_name(),int(st.get_score()), int(st.get_score()), int(st.get_score()), int(st.get_score()),int(st.get_score())])

    filesize = os.path.getsize(filename)
    client.send(f"{filesize}".encode())
    # with open(filename, 'rb') as f:
    #     while True:
    #         bytes_read = f.read(HEADER)
    #         # print("bytes_read")
    #         if not bytes_read:
    #             print("out of loop")
    #             break
    #
    #         client.sendall(bytes_read)
    #         # client.send(bytes_read)
    #         print("bytes_read")

    f = open(filename, 'rb')
    l = f.read(HEADER)
    while l:
        client.send(l)
        l = f.read(HEADER)
    f.close()

    print(filesize, "done !")

while True:
    print("send, sendcsv , avg, sort, max, min,  server, end")
    command = input()
    client.send(command.encode())
    if command == "send":
        send_string2()

    if command == "sendcsv":
        file_name = input("enter the name of file example file.csv: ")
        send_csv(file_name)

    elif command == "avg":
        stat = client.recv(HEADER)
        print(stat.decode())

    elif command == "sort":
        for i in range(FILE_SIZE+1):
            sort_id = client.recv(HEADER)
            print(sort_id.decode())

    elif command == "max":
        for i in range(2):
            max_name = client.recv(HEADER)
            print(max_name.decode())

    elif command == "server":
        server_message = client.recv(HEADER)
        print(server_message.decode())

    elif command == "min":
        for i in range(2):
            min_name = client.recv(HEADER)
            print(min_name.decode())

    elif command == "end":
        print("byby")
        client.close()
        break


    else :
        print("command is wrong try again")