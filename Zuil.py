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

root = Tk()

root.title('ns beoordelingen')
root.geometry("800x400")
root.configure(bg='yellow')
p1 = PhotoImage(file='Illustratie_blog_algemeen_NS_Tekengebied-1-500x500.png')
root.iconphoto(False, p1)

label = Label(master = root,
              text = 'NS',
              background = 'yellow',
              foreground= 'blue',
              font=('Ariel', 16, 'bold italic'))

label.pack()

label2=Label(master=root,
             text ='vul hier je beoordeling in:',
             background = 'yellow',
             foreground= 'black',
             font = ('ariel',16,'bold italic'))
label2.pack()
berichtlabel =Label(master=root,
            text = 'Bericht:',
            background = 'yellow',
            foreground= 'black',
            font = ('ariel',8,'bold italic'))
berichtlabel.pack(pady=(10,2),padx=(10,15))

berichtlabel.pack()
#enter= Button(master=root,text='Enter', command = )
#button.pack(pady=50)

w = Entry(master=root)
w.pack(pady=0,padx=15)

root.mainloop()