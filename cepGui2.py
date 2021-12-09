from tkinter import *
from cepFileSaver1 import *

root = Tk()
root.geometry("600x500")
root.title("reinforcement")
frame = Frame(root)
frame.pack()
message = StringVar()
message.set("Title")
label = Label(frame, textvariable = message)
label.pack()
mainmenu = Menu(root)
filemenu = Menu(mainmenu, tearoff = 0)

filemenu.add_command(label = "Exit", command = root.destroy)
mainmenu.add_cascade(label="File", menu=filemenu)


root.config(menu = mainmenu)

root.mainloop()