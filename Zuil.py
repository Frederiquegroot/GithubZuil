from datetime import datetime
import random
import psycopg2
from tkinter import *
def stationzuil():
    """

    :return:
    """
    now = datetime.now()
    data = now.strftime("%m/%d/%Y;%H:%M:%S") #tijd en datum bij de beoordeling

    stations = ('Oss','Sittard','Zwolle')
    station = random.choice(stations)  #zorgt dat elke mening een random station krijgt toegewezen in het txt bestand

    naam = input('wat is je naam?') # naam invullen en als ze geen naam in hebben gevuld anoniem
    if naam == '':
       naam = 'Anoniem'

    mening = input('wat is jou mening?')

    if len(mening) > 140 or ';' in mening:  #mening checken of die te lang is en of ; bevat en als dat zo is foutcode
      print('je mening is te lang! of bevat ;' )


    else:
        outfile = open ('Mening.txt', 'a')
        outfile.write(naam+';'+mening+';'+data+';'+station+'\n') # zorgt dat als alles goed is met de mening en schrijft die in het txt bestand netjes achter elkaar
        print(naam+';'+mening+';'+data+';'+station)
stationzuil()





