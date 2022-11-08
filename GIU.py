from datetime import datetime
import random
import psycopg2
from tkinter import *
import requests
def weatherstationscherm(stationscherm):
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
    weatherapp= requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=91f9f5a862c793cc643e4a1227221baf')
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
for record in records:
    print(record[0])

root.title('ns beoordelingen')
root.geometry("800x400")
root.configure(bg='yellow')
p1 = PhotoImage(file='Illustratie_blog_algemeen_NS_Tekengebied-1-500x500.png')
root.iconphoto(False, p1)


root.mainloop()

