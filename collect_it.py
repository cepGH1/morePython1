from tkinter import *
from cepFileSaver1 import *

questions =[]
correctAnswers = []
fa1s =[]
fa2s =[]
fa3s =[]
myCheck =""

def save1():
    pass

def appendToList(question, fa1, fa2, fa3, answer):
    questions.append(question)
    correctAnswers.append(answer)
    fa1s.append(fa1)
    fa2s.append(fa2)
    fa3s.append(fa3)

def getLists(questionNumber):
    pass    



root = Tk()
root.geometry("800x800")
root.title("collect it")
frame = Frame(root)
frame.pack()
message = StringVar()
message.set("Title")
message1 = StringVar()
message1.set("Question")
message3 = StringVar()
message3.set("Possible Answers")
message4 = StringVar()
message4.set("Correct Answer")
message5 = StringVar()
message5.set("What do you want to do with your entries")
label = Label(frame, textvariable = message)
label.pack()
questionFrame =Frame(frame, bg="yellow")
label2 = Label(questionFrame, textvariable=message1)
label2.pack()
inputBox = Text(questionFrame, bg="pink", height="5")
inputBox.pack()
questionFrame.pack(side=TOP)
answersFrame = Frame(frame)
label3 = Label(answersFrame, textvariable=message3)
label3.pack()
inputBox2 = Text(answersFrame, bg="blue", height="5")
inputBox2.pack()
inputBox3 = Text(answersFrame, bg="green", height="5")
inputBox3.pack()
inputBox4 = Text(answersFrame, bg="white", height="5")
inputBox4.pack()
answersFrame.pack(side=TOP)
correctAnswerFrame = Frame(frame)
label4 = Label(correctAnswerFrame, textvariable=message4)
label4.pack()
inputBox5 = Text(correctAnswerFrame, bg="violet", height="5")
inputBox5.pack()
correctAnswerFrame.pack(side=TOP)
controlFrame = Frame(frame)

label5 = Label(controlFrame, textvariable=message5)
label5.pack()
saveButton1 = Button(controlFrame, text="save all", command=save1)
saveButton1.pack()
saveButton2 = Button(controlFrame, text="Add to quiz", command=appendToList(inputBox.get("1.0"), inputBox2.get("1.0"), inputBox3.get("1.0"), inputBox4.get("1.0"), inputBox5.get("1.0")))
saveButton2.pack()
checkButton = Button(controlFrame, text="check")
checkButton.pack()
controlFrame.pack(side=BOTTOM)
mainmenu = Menu(root)
filemenu = Menu(mainmenu, tearoff = 0)

filemenu.add_command(label = "Exit", command = root.destroy)
mainmenu.add_cascade(label="File", menu=filemenu)


root.config(menu = mainmenu)

root.mainloop()

