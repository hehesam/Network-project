import socket
import threading
import subprocess
import os
import pandas
import pandas as pd
from IPython.display import display


HEADER = 10240
PORT = 65430

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "DISCONNECT!"
SEPARATOR = "<SEPARATOR>"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(server)


def show_data(filename):
    df = pd.read_csv(filename)
    display(df)
    return df


def avg_data(df):
    display(df)
    avg = []
    for index, row in df.iterrows():
        res = (row['score1']+row['score2']+row['score3']+row['score4']+row['score5'])/5
        avg.append(res)
    df['AVG'] = avg

    display(df)
    return df


def sort_data(df):
    sorted_data = df.sort_values(by='AVG')
    display(sorted_data)
    return sorted_data


def max_data(df):
    max_avg = df.iloc[-1]['AVG']
    max_name = df.iloc[-1]['name']
    return (max_name,max_avg)


def min_data(df):
    min_avg = df.iloc[0]['AVG']
    min_name = df.iloc[0]['name']
    return (min_name,min_avg)


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    data_base = pd.DataFrame()
    new_filename = ""
    while True:
        print("send_csv , avg, sort, max, min, end")
        command = conn.recv(HEADER).decode()
        print("read command : ", command)
        if command == 'sendcsv':
            filename = conn.recv(HEADER).decode()
            filesize = conn.recv(HEADER).decode()
            print(filename,filesize)
            new_filename = "se"+filename
            f = open(new_filename, 'wb')
            l = conn.recv(int(filesize))
            f.write(l)
            f.close()
            data_base = show_data(new_filename)

        elif command == 'avg':
            data_base = avg_data(data_base)
            data_base.to_csv(new_filename)
            filesize = os.path.getsize(new_filename)

            conn.send(new_filename.encode())
            conn.send(str(filesize).encode())

            f = open(new_filename, 'rb')
            l = f.read(HEADER)
            while l:
                conn.send(l)
                l = f.read(HEADER)
            f.close()

        elif command == 'sort':
            data_base = sort_data(data_base)
            data_base.to_csv(new_filename)
            filesize = os.path.getsize(new_filename)

            conn.send(new_filename.encode())
            conn.send(str(filesize).encode())

            f = open(new_filename, 'rb')
            l = f.read(HEADER)
            while l:
                conn.send(l)
                l = f.read(HEADER)
            f.close()

        elif command == "max":
            name, score = max_data(data_base)
            conn.send(f"the smartkid : {name}, score: {score}".encode())

        elif command == "min":
            name, score = min_data(data_base)
            conn.send(f"the dumb kid : {name}, score: {score}".encode())



        elif command == 'end' or command == '':
            print("client disconnected")
            conn.close()
            break
        else:
            print("command is wrong try again")




def start(client_number):

    server.listen()
    for i in range(client_number):
        subprocess.call(["gnome-terminal" , "--" , "sh", "-c", "python3 client.py"])

    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


client_number = int(input("how many client ?"))
start(client_number)