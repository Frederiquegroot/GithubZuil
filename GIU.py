from datetime import datetime
import random
import psycopg2
from tkinter import *
import requests
import json
from PIL import Image,ImageTk
def weatherstationscherm():
    stationscherm=input('op welk station ben je?')
    if stationscherm == 'zwolle' or stationscherm == 'oss' or stationscherm == 'sittard':
        if stationscherm == 'zwolle':
            lon = '6.0830219'
            lat = '52.5167747'
        elif stationscherm  == 'oss':
            lon = '5.5140482'
            lat = '51.7611801'
        elif stationscherm == 'sittard':
            lon = '5.8864788'
            lat= '51.0006238'
    else:
        print('vul een geldig station in')
    weatherapp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=nl&appid=bf86466a3e5f7265d40460a017a86ae6')
    omschrijving = json.loads(weatherapp.text)['weather']
    weerbericht= json.loads(weatherapp.text)['main']
    print(omschrijving[0]['description'])
    print(weerbericht['temp'],'C')
    print(omschrijving)

    root = Tk()

    connection_string = "host='localhost' dbname='zuilfa3' user='postgres' password='Molly123fred!'"
    conn = psycopg2.connect(connection_string)  # get a connection with the database
    cursor = conn.cursor()
    query = """select naamMening,bericht,datum,tijd,bericht.stationstad,station.ovfiets,station.lift,station.pr,station.toilet from bericht 
    inner join station on station.stationstad = bericht.stationstad
    order by "beoordelingid" desc limit 5;""" # the string

    cursor.execute(query)
    records = cursor.fetchall() # retrieve the records from the database
    conn.close()
    print(records)
    r=2

    for record in records:
        #print(record[0])
        c=0
        p=0
        for item in record:

            if item == True and item == 1 or item == False:

                p+=1
                faciliteit = ''
                if item == True and p == 1:
                    print(1)
                    faciliteit = 'ovfiets'
                    c += 1
                elif item == True and p == 2:
                    faciliteit = 'lift'
                    print(2)
                    c += 1
                elif item == True and p == 3:
                    print(3)
                    faciliteit = 'pr'
                    c += 1
                elif item == True and p == 4:
                    print(4)
                    faciliteit = 'toilet'
                    c += 1

                if faciliteit != '':
                    image = Image.open(f"img_{faciliteit}.png")
                    resize_image = image.resize((75, 64))

                    img = ImageTk.PhotoImage(resize_image)
                    label = Label(image=img)
                    label.image = img  # keep a reference!
                    label.grid(row=r, column=c, pady=5, padx=5)
                    faciliteit = ''






            else:

                label1=Label(master=root,
                             text=item,
                             fg='blue',
                             bg='yellow',
                             font=('Ariel', 10))
                label1.grid(row=r,column=c)
                c+=1
        r+=1
        b=0
        for  n in ('Naam','Bericht','Datum','Tijd','Station'):
            label2 = Label(master=root,
                           text=n,
                           fg='blue',
                           bg='yellow',
                           font=('Ariel', 20))

            label2.grid(row=1,column=b)
            b+=1
        label3= Label(master=root,
                      text='faciliteiten',
                      fg='blue',
                      bg='yellow',
                      font=('Ariel',20))
        label3.grid(row=1,column=5,columnspan=4)

        label4= Label(master=root,
                      text=stationscherm,
                      fg='blue',
                      bg='yellow',
                      font=('Ariel',30))
        label4.grid(row=0,column=0)

        label5= Label(master=root,
                      text=omschrijving[0]['description']+'\n'+str(round(weerbericht['temp'],1))+'C',
                      fg='blue',
                      bg='yellow',
                      font=('Ariel',20))
        label5.grid(row=0, column=1)


    root.title('ns beoordelingen')
    root.geometry("800x400")
    root.configure(bg='yellow')
    p1 = PhotoImage(file='Illustratie_blog_algemeen_NS_Tekengebied-1-500x500.png')




    root.iconphoto(False, p1)


    root.mainloop()

weatherstationscherm()

