from datetime import datetime
import random
naam = input('wat is je naam?')
if naam == '':
    naam = 'Anoniem'

mening = input('wat is jou mening?')

now = datetime.now()
data = now.strftime("%m/%d/%Y, %H:%M:%S")

Stations = ('Zwolle','Sittard','Oss')

outfile = open ('Mening.txt', 'a')
outfile.write(naam)
outfile.write('\n')
outfile.write(mening)
outfile.write('\n')
outfile.write(data)
outfile.write('\n')
print(naam+'\n'+mening+'\n'+data)