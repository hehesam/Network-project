import socket
<<<<<<< HEAD


import random
from random import randint


def create_name():
    first_name = ["Liam","Emma","Charlotte","Oliver","Elijah","James","Benjamin","Harper","Levi","Elizabeth","Daniel","Sofia","Mason","Logan","Layla","John","Joseph","Lily","Violet","Riley","Isaac","Stella","Victoria","Piper","Peyton","Sadie"]
    last_name = ["Levin","Kennedy","James","Hayley","Hayden","Greer","Everly","Darcy","Colby","Alexander","Anderson","Alder","Bentley","Beck","Birk","Blake","Byron","Carson","Emerson","Finley","Griffin","Holden","Hudson","Jackson","Kiefer","Kingsley","Landon","Logan","Marshall","Mercer","Miller"]

    res = random.choice(tuple(first_name)) + " " + random.choice(tuple(last_name))
    return res

def create_na_id():
    res = str(randint(1200000000,1299999999))
    return res

def create_st_id():
    res = str(randint(900000000,999999999))
    return res

def score():
    return str(randint(13, 20))

def create():
    res = create_na_id() + " " + create_st_id() + " " + create_name()  + " " + score()
    return res


=======
from data_maker import create
>>>>>>> 0fab17329a3050297772b18c84c980a952b92321
HEADER = 64
PORT = 65432
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):

    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '* (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)


    

print("You can chat 3 times : ")
for i in range(3):
<<<<<<< HEAD
    print(create())
=======
>>>>>>> 0fab17329a3050297772b18c84c980a952b92321
    send(create())
    send(input())
send(DISCONNECT_MESSAGE)
