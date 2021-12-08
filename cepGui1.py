from tkinter import *

def getChoice():
    myChoice = textBox.curselection()
    myStringyChoice = textBox.get(myChoice)
    print(myStringyChoice)

def getNotes():
    note1 = inputBox.get()
    print(note1)
def save():
    pass
def load():
    pass

root = Tk()
root.geometry("500x500")
frame = Frame(root)
frame.pack()
mainmenu = Menu(frame)
mainmenu.add_command(label = "Save", command= save)  
mainmenu.add_command(label = "Load", command= load)
mainmenu.add_command(label = "Exit", command= root.destroy)
 
root.config(menu = mainmenu)
 
leftframe = Frame(root, bg="red")
leftframe.pack(side=LEFT)
 
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
 
label = Label(frame, text = "Hello world")
label.pack()
textBox = Listbox(frame)
textBox.insert(1, "atomic")
textBox.insert(2, "salomen")
textBox.pack()
inputBox = Entry(frame, bg="pink")
inputBox.pack()
 
button1 = Button(leftframe, text = "submit ski choice", command=getChoice)
button1.pack(padx = 3, pady = 3)
button2 = Button(rightframe, text = "Button2")
button2.pack(padx = 3, pady = 3)
button3 = Button(leftframe, text = "add notes", command=getNotes)
button3.pack(padx = 3, pady = 3)
 
root.title("Test")
root.mainloop()

