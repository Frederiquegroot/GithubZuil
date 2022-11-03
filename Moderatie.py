from datetime import datetime
import random
import psycopg2
from tkinter import *
def psycopg2():
    connection_string= "host='localhost' dbname='zuil' FA user='postgres' password='geheim'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    insert="INSERT INTO beoordeling values()"


    cursor.execute(insert)
    #records = cursor.fetchall()
    conn.close

def moderatie():
    now = datetime.now()
    data = now.strftime("%m/%d/%Y %H:%M:%S")

    outfile = open('mening.txt', 'r')
    regels = outfile.readlines()
    nmoderator = input('wat is je naam:')
    emailmoderator = input('wat is je email:')
    for regel in regels:
        berichtmening = regel.split(';')

        print(berichtmening[0])
        print(berichtmening[1])
        beoordeling = input('typ y voor goedgekeurd en n voor foutgekeurd: ')


    if beoordeling == 'y':
      outfile= open('Mening.txt', 'a')
      outfile.write(nmoderator + ';' + emailmoderator + ';' + data +';' + beoordeling + ';' + '\n')
      print(nmoderator + ';' + emailmoderator + ';'+ data + ';' + beoordeling + ';')

    elif beoordeling =='n':
     outfile = open('Mening.txt', 'a')
     outfile.write(nmoderator + ';' + emailmoderator + ';' + data + ';' + beoordeling + ';' + '\n')
     print(nmoderator + ';' + emailmoderator + ';' + data + ';' + beoordeling + ';')

    else:
        print('typ alleen y of n in')

    outfile.close()
    outfile= open('mening.txt','w')
    outfile.close()

moderatie()