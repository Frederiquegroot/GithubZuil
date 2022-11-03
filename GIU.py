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


w = Entry(master=root)
w.pack(pady=0,padx=15)

root.mainloop()