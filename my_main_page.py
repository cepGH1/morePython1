import tkinter as tk

from quiz_designer1 import QuizDesigner

def designQuiz():
    
    clare = QuizDesigner()
    clare.runQuiz()
    


    

root = tk.Tk()
root.geometry("600x600")
root.title("Main")
frame = tk.Frame(root, height=100, width=100, bg="white")

frame.pack(fill="both", expand=True)
topFrame = tk.Frame(frame)
topFrame.pack( fill="both", expand=True)
bottomFrame = tk.Frame(frame)
bottomFrame.pack( fill="both", expand=True)
entryFrame = tk.Frame(topFrame, bg="red", )
entryMessage = tk.StringVar()
entryMessage.set("Make a quiz here")
entryLabel = tk.Label(entryFrame, textvariable= entryMessage)
entryLabel.pack()
entryButtonMessage = tk.StringVar()
entryButtonMessage.set("Start a New Quiz")
entryButton = tk.Button(entryFrame, textvariable= entryButtonMessage, command=designQuiz())
entryButton.pack()
entryFrame.pack(fill='both',  expand=True)
infoFrame = tk.Frame(topFrame, bg="purple")
infoFrame.pack( fill="both", expand=True)
infoMessage = tk.StringVar()
infoMessage.set("This frame is for information")

infoLabel = tk.Label(infoFrame, textvariable=infoMessage)
infoLabel.pack()

listFrame = tk.Frame(bottomFrame, bg="cyan")
listFrame.pack(fill="both", expand=True)
listMessage = tk.StringVar()
listMessage.set("Available quizzes")
listLabel = tk.Label(listFrame, textvariable=listMessage)
listLabel.pack()
playFrame = tk.Frame(bottomFrame, bg="yellow")
playMessage = tk.StringVar()
playMessage.set("Run a quiz here")
playLabel = tk.Label(playFrame, textvariable= playMessage)
playLabel.pack()
playButtonMessage = tk.StringVar()
playButtonMessage.set("Load a Quiz")
playButton = tk.Button(playFrame, textvariable= playButtonMessage)
playButton.pack()
playFrame.pack(fill="both", expand=True)



mainmenu = tk.Menu(root)
filemenu = tk.Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "save")
filemenu.add_command(label = "Exit", command = root.destroy)
mainmenu.add_cascade(label="File", menu=filemenu)


root.config(menu = mainmenu)
root.mainloop()


    