from datetime import datetime
import random
import psycopg2
from tkinter import *
def stationzuil():
    """

    :return:
    """
    now = datetime.now()
    data = now.strftime("%m/%d/%Y %H:%M:%S")

    stations = ('Zwolle','Sittard','Oss')
    station = random.choice(stations)

    naam = input('wat is je naam?')
    if naam == '':
       naam = 'Anoniem'

    mening = input('wat is jou mening?')

    if len(mening) > 140 or ';' in mening:
      print('je mening is te lang! of bevat ;' )


    else:
        outfile = open ('Mening.txt', 'a')
        outfile.write(naam+';'+mening+';'+data+';'+station+'\n')
        print(naam+';'+mening+';'+data+';'+station)
stationzuil()

def moderatie():
    outfile = open('mening.txt', 'r')
    regels = outfile.readlines()
    for regel in regels:
        berichtInfo = regel.split(';')
        print(berichtInfo)
        bericht = berichtInfo[1]

        print(bericht)
        nmoderator= input('wat is je naam:')
        emailmoderator=input('wat is je email:')
        beoordeling = input('typ y voor goedgekeurd en n voor foutgekeurd: ')


    if beoordeling == 'y':
      outfile= open('Mening.txt', 'a')
      outfile.write(nmoderator + ';' +emailmoderator  + ';' + beoordeling + ';' + '\n')
      print(nmoderator+ ';' + emailmoderator + ';' + beoordeling+ ';')

    else:
     beoordeling =='n'
     outfile = open('Mening.txt', 'a')
     outfile.write(nmoderator + ';' + emailmoderator + ';' + beoordeling + ';' + '\n')
     print(nmoderator + ';' + emailmoderator + ';' + beoordeling + ';')
moderatie()
