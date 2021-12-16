#a class to handle data entry for the quiz app
import tkinter as fk

class QuizDesigner:
    questions =[]
    correctAnswers = []
    fa1s =[]
    fa2s =[]
    fa3s =[]
    myquizReport = False

    def __init__(self):
        self.questions =[]
        self.correctAnswers=[]
        self.fa1s=[]
        self.fa2s=[]
        self.fa3s=[]
        self.myQuizReport =False

    def runQuiz(self):
        frog = fk.Tk()
        frog.geometry("800x800")
        frog.title("collect it")
        frame = fk.Frame(frog)
        frame.pack()
        message = fk.StringVar()
        message.set("Put questions and answers in here to construct a multiple choice test")
        message1 = fk.StringVar()
        message1.set("Question")
        message3 = fk.StringVar()
        message3.set("Possible Answers")
        message4 = fk.StringVar()
        message4.set("Correct Answer")
        message5 = fk.StringVar()
        message5.set("What do you want to do with your entries")
        label = fk.Label(frame, textvariable = message)
        label.pack()
        questionFrame =fk.Frame(frame, bg="yellow")
        label2 = fk.Label(questionFrame, textvariable=message1)
        label2.pack()
        inputBox = fk.Text(questionFrame, bg="pink", height="5")
        inputBox.pack()
        questionFrame.pack()
        answersFrame = fk.Frame(frame)
        label3 = fk.Label(answersFrame, textvariable=message3)
        label3.pack()
        inputBox2 = fk.Text(answersFrame, bg="blue", height="5")
        inputBox2.pack()
        inputBox3 = fk.Text(answersFrame, bg="green", height="5")
        inputBox3.pack()
        inputBox4 = fk.Text(answersFrame, bg="white", height="5")
        inputBox4.pack()
        answersFrame.pack()
        correctAnswerFrame = fk.Frame(frame)
        label4 = fk.Label(correctAnswerFrame, textvariable=message4)
        label4.pack()
        inputBox5 = fk.Text(correctAnswerFrame, bg="violet", height="5")
        inputBox5.pack()
        correctAnswerFrame.pack()
        controlFrame = fk.Frame(frame)

        label5 = fk.Label(controlFrame, textvariable=message5)
        label5.pack()
        saveButton1 = fk.Button(controlFrame, text="save all", command=self.save1)
        saveButton1.pack( padx=10)
        saveButton2 = fk.Button(controlFrame, text="Add to quiz", command=self.appendToList)
        saveButton2.pack( padx=10)
        checkButton = fk.Button(controlFrame, text="show all questions and answers", command=self.showQuiz)
        checkButton.pack( padx=10)
        controlFrame.pack()
        #mainmenu = Menu(root)
        #filemenu = Menu(mainmenu, tearoff = 0)
        #filemenu.add_command(label = "save", command= saveWindow)
        #filemenu.add_command(label = "Exit", command = root.destroy)
        #mainmenu.add_cascade(label="File", menu=filemenu)


        #root.config(menu = mainmenu)

        frog.mainloop()
    
    def save1(self):
        content1 = self.saveMyList1(self.questions, self.fa1s, self.fa2s, self.fa3s, self.correctAnswers)
        self.saveMyList2(content1, "test3.txt")
    
    def showQuiz(self):
        content1 = self.saveMyList1(self.questions, self.fa1s, self.fa2s, self.fa3s, self.correctAnswers)
    
        quizReport = fk.Tk()
        quizReport.geometry("400x400")
        quizFrame = fk.Frame(quizReport)
        quizFrame.pack()
        reportContent =fk.StringVar()
        reportContent.set(content1)
        report = fk.Text(quizFrame)

        report.insert("1.0", content1)
    
        report.pack()

    def appendToList(self):
    
        question = self.inputBox.get("1.0", "end - 1 chars")
        answer = self.inputBox5.get("1.0", "end - 1 chars")
        fa1 = self.inputBox2.get("1.0", "end - 1 chars")
        fa2 = self.inputBox3.get("1.0", "end - 1 chars")
        fa3 = self.inputBox4.get("1.0", "end - 1 chars")
        self.questions.append(question)
        self.correctAnswers.append(answer)
        self.fa1s.append(fa1)
        self.fa2s.append(fa2)
        self.fa3s.append(fa3)