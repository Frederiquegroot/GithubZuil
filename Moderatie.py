from datetime import datetime
import random
import psycopg2
from tkinter import *
def psycopg2(naamMening,bericht,datum,tijd,station_stad,tijdBeoordeling,datumBeoordeling,naamModerator):


    connection_string= "host='localhost' dbname='zuil FA' user='postgres' password='Molly123fred!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    insert="""INSERT INTO bericht values(beoordelingID,naamMening,tijd,datum,tijdBeoordeling,DatumBeoordeling,station_stad,naamModerator,bericht)
            values(DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s)"""


    data = (naamMening,tijd,datum,tijdBeoordeling,datumBeoordeling,station_stad,naamModerator,bericht)
    cursor.execute(insert, data)
    conn.commit()
    conn.close()

def moderatie():
    now = datetime.now()
    databeoordeling = now.strftime("%m/%d/%Y;%H:%M:%S")
    datumbeoordeling = databeoordeling.split(';')[0]
    tijdbeoordeling = databeoordeling.split(';')[1]

    outfile = open('mening.txt', 'r')
    regels = outfile.readlines()
    moderator = input('wat is je naam:')
    emailmoderator = input('wat is je email:')
    for regel in regels:
        berichtmening = regel.split(';')

        print(berichtmening[0])
        print(berichtmening[1])
        beoordeling = input('typ y voor goedgekeurd en n voor foutgekeurd: ')


    if beoordeling == 'y':
        psycopg2(berichtmening[0], berichtmening[1], berichtmening[2], berichtmening[3], berichtmening[4],
                 tijdbeoordeling, datumbeoordeling, moderator)


    elif beoordeling =='n':
       outfile = open('Mening.txt', 'a')
       outfile.write(moderator + ';' + emailmoderator + ';' + databeoordeling + ';' + beoordeling + ';' + '\n')
       print(moderator + ';' + emailmoderator + ';' + databeoordeling + ';' + beoordeling + ';')

    else:
        print('typ alleen y of n in')

    outfile.close()
    #outfile= open('mening.txt','w')
    #outfile.close()

moderatie()