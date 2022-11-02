from tkinter import *
#from PIL import ImageTK, image

root = Tk()

#img = ImageTK.PhotoImage(file = 'scsweb.png')

def onclick():
    base = int(entry.get())
    square = base ** 2
    outcome = f'square of: {base} = {square}'
    label['text'] = outcome

label = Label(master = root,
              text = 'howi',
              background = 'pink',
              foreground= 'purple',
              font=('Ariel', 16, 'bold italic'),
              width = 15,
              height = 8,)
label.pack()

button = Button(master=root,text='press', command = onclick)

button.pack(pady=50)

entry = Entry(master=root)
entry.pack(pady=10, padx=10)

root.mainloop()