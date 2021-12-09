from tkinter import *
from cepFileSaver1 import *

questions =[]
correctAnswers = []
fa1s =[]
fa2s =[]
fa3s =[]
myquizReport = False

def save1():
    content1 = saveMyList1(questions, fa1s, fa2s, fa3s, correctAnswers)
    saveMyList2(content1, "test3.txt")
    

def appendToList():
    
    question = inputBox.get("1.0", "end - 1 chars")
    answer = inputBox5.get("1.0", "end - 1 chars")
    fa1 = inputBox2.get("1.0", "end - 1 chars")
    fa2 = inputBox3.get("1.0", "end - 1 chars")
    fa3 = inputBox4.get("1.0", "end - 1 chars")
    questions.append(question)
    correctAnswers.append(answer)
    fa1s.append(fa1)
    fa2s.append(fa2)
    fa3s.append(fa3)
    

def getLists(questionNumber):
    pass    

def saveWindow():
    save1()

def showQuiz():
    content1 = saveMyList1(questions, fa1s, fa2s, fa3s, correctAnswers)
    
    quizReport = Tk()
    quizReport.geometry("400x400")
    quizFrame = Frame(quizReport)
    quizFrame.pack()
    report = Text(quizFrame)
    report.insert("1.0", content1)
    
    report.pack()
    

    
    


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
saveButton1.pack(side=LEFT, padx=10)
saveButton2 = Button(controlFrame, text="Add to quiz", command=appendToList)
saveButton2.pack(side=LEFT, padx=10)
checkButton = Button(controlFrame, text="show all questions and answers", command=showQuiz)
checkButton.pack(side=LEFT, padx=10)
controlFrame.pack(side=BOTTOM)
mainmenu = Menu(root)
filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "save", command= saveWindow)
filemenu.add_command(label = "Exit", command = root.destroy)
mainmenu.add_cascade(label="File", menu=filemenu)


root.config(menu = mainmenu)

root.mainloop()

