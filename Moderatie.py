from datetime import datetime
import random
import psycopg2
from tkinter import *
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
            psycopg(berichtmening[0], berichtmening[1], berichtmening[2], berichtmening[3], berichtmening[4],
                 tijdbeoordeling, datumbeoordeling, moderator)
        elif beoordeling =='n':
            print('.')
        else:
            print('typ alleen y of n in')

    outfile.close()
    #outfile= open('mening.txt','w')
    #outfile.close()

moderatie()