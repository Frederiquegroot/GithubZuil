from datetime import datetime
import random

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

    if len(mening) > 140:
        print('je mening is te lang!')
    else:
        outfile = open ('Mening.txt', 'a')
        outfile.write(naam+'|'+mening+'|'+data+'|'+station+'\n')
        print(naam+'|'+mening+'|'+data+'|'+station)
#def moderator():