from tkinter import *


root = Tk()
root.geometry("600x600")
root.title("Main")
frame = Frame(root, height=100, width=100, bg="white")

frame.pack(fill="both", expand=True)
topFrame = Frame(frame)
topFrame.pack(side=TOP, fill="both", expand=True)
bottomFrame = Frame(frame)
bottomFrame.pack(side=BOTTOM, fill="both", expand=True)
entryFrame = Frame(topFrame, bg="red", )
entryMessage = StringVar()
entryMessage.set("Make a quiz here")
entryLabel = Label(entryFrame, textvariable= entryMessage)
entryLabel.pack()
entryButtonMessage = StringVar()
entryButtonMessage.set("Start a New Quiz")
entryButton = Button(entryFrame, textvariable= entryButtonMessage)
entryButton.pack()
entryFrame.pack(fill='both', side=LEFT, expand=True)
infoFrame = Frame(topFrame, bg="purple")
infoFrame.pack(side=LEFT, fill="both", expand=True)
infoMessage = StringVar()
infoMessage.set("This frame is for information")

infoLabel = Label(infoFrame, textvariable=infoMessage)
infoLabel.pack()

listFrame = Frame(bottomFrame, bg="cyan")
listFrame.pack(fill="both", side=LEFT, expand=True)
listMessage = StringVar()
listMessage.set("Available quizzes")
listLabel = Label(listFrame, textvariable=listMessage)
listLabel.pack()
playFrame = Frame(bottomFrame, bg="yellow")
playMessage = StringVar()
playMessage.set("Run a quiz here")
playLabel = Label(playFrame, textvariable= playMessage)
playLabel.pack()
playButtonMessage = StringVar()
playButtonMessage.set("Load a Quiz")
playButton = Button(playFrame, textvariable= playButtonMessage)
playButton.pack()
playFrame.pack(fill="both", side=LEFT, expand=True)



mainmenu = Menu(root)
filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "save")
filemenu.add_command(label = "Exit", command = root.destroy)
mainmenu.add_cascade(label="File", menu=filemenu)


root.config(menu = mainmenu)
root.mainloop()

