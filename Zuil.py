from datetime import datetime
import random
naam = input('wat is je naam?')
if naam == '':
    naam = 'Anoniem'

mening = input('wat is jou mening?')

now = datetime.now()
data = now.strftime("%m/%d/%Y,%H:%M:%S")

stations = ('Zwolle','Sittard','Oss')
station = random.choice(stations)

outfile = open ('Mening.txt', 'a')
outfile.write(naam+';'+mening+';'+data+';'+station)
print(naam+';'+mening+';'+data+';'+station)