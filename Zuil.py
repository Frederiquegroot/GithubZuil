from datetime import datetime
naam = input('wat is je naam?')
mening = input('wat is jou mening?')

now = datetime.now()
data = now.strftime("%m/%d/%Y, %H:%M:%S")

outfile = open ('Mening.txt', 'a')
outfile.write(naam)
outfile.write('\n')
outfile.write(mening)
outfile.write('\n')
outfile.write(data)
outfile.write('\n')
print(naam+'\n'+mening+'\n'+data)