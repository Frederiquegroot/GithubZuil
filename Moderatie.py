from datetime import datetime
import random
import psycopg2
from tkinter import *

# dit zorgt dat de database in sql is gekoppeld aan dit python bestand zodat als er de meningen beoordeeld zijn en goedgekeurd kunnen ze in de database worden geinsert
def psycopg(naammening,bericht,datum,tijd,stationstad,tijdbeoordeling,datumbeoordeling,naammoderator):


    connection_string= "host='localhost' dbname='zuilfa3' user='postgres' password='Molly123fred!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    insert="""INSERT INTO bericht(beoordelingid,naammening,tijd,datum,tijdbeoordeling,Datumbeoordeling,stationstad,naammoderator,bericht) 
            VALUES(DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s)"""


    data = (naammening,tijd,datum,tijdbeoordeling,datumbeoordeling,stationstad.split('\n')[0],naammoderator,bericht)
    cursor.execute(insert,data)
    conn.commit()
    conn.close()

def moderatie():
    now = datetime.now()
    databeoordeling = now.strftime("%m/%d/%Y;%H:%M:%S")
    datumbeoordeling = databeoordeling.split(';')[0]
    tijdbeoordeling = databeoordeling.split(';')[1]

    outfile = open('mening.txt', 'r')  # haalt de mening uit het txt bestand en split het zodat ze alleen de naam en het bericht zien
    regels = outfile.readlines()
    moderator = input('wat is je naam:')
    emailmoderator = input('wat is je email:')
    for regel in regels:
        berichtmening = regel.split(';')

        print(berichtmening[0])
        print(berichtmening[1])
        beoordeling = input('typ y voor goedgekeurd en n voor foutgekeurd: ')


        if beoordeling == 'y':
            psycopg(berichtmening[0], berichtmening[1], berichtmening[2], berichtmening[3], berichtmening[4],
                 tijdbeoordeling, datumbeoordeling, moderator) # zorgt dat als het is goedgekeurd het netjes in de database wordt gezet
        elif beoordeling =='n':
            print('.')
        else:
            print('typ alleen y of n in') # foutmelding als ze geen y of n typen

    outfile.close()
    outfile= open('mening.txt','w')  #maakt de hele file leeg nadat alles is beoordeeld
    outfile.close()

moderatie()