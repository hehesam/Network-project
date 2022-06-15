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
    return randint(13, 20)

def create():
    return create_na_id + " " + create_st_id + " " + create_name  + " " + score