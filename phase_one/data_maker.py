
from random import *
import random

first_name = ["Liam","Emma","Charlotte","Oliver","Elijah","James","Benjamin","Harper","Levi","Elizabeth","Daniel","Sofia","Mason","Logan","Layla","John","Joseph","Lily","Violet","Riley","Isaac","Stella","Victoria","Piper","Peyton","Sadie"]
last_name = ["Levin","Kennedy","James","Hayley","Hayden","Greer","Everly","Darcy","Colby","Alexander","Anderson","Alder","Bentley","Beck","Birk","Blake","Byron","Carson","Emerson","Finley","Griffin","Holden","Hudson","Jackson","Kiefer","Kingsley","Landon","Logan","Marshall","Mercer","Miller"]



def name_generator():
    res = random.choice(tuple(first_name)) + " " + random.choice(tuple(last_name))
    return res
def st_id_generator():
    res = "ST" + str(randint(90000000,99999999))
    return res

def na_id_generator():
    res = str(randint(1000000000,1299999999))
    return res


def score():
    return str(randint(13,20))






def create():
    res = ""
    for i in range(5):
        res += score() + " "

    return na_id_generator()+ " "+ st_id_generator()+ " " + name_generator() + " " + res



