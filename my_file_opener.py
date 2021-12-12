#open the file

#read the contents to a string


#slice the string into indivual strings starting at each occurance of question

#slice each question string into question string, answers Dict

answers = {}
questionString =""
contentsString =""

def openMyFile(fileName):
    myReadFile = open(fileName, "r")
    contentsString = myReadFile.read()
    print(contentsString)
    myReadFile.close()
    return contentsString

def getQuestion(fileName):
    myFileString = openMyFile(fileName)
    contentsList = myFileString.splitlines()
    return contentsList
#returns a list of the questions in the storage text file
def makeQuestionList(fileName):
    questionsList =[]
    contentsList = getQuestion(fileName)
    x = 1
    while(x < len(contentsList)):
        questionsList.append(contentsList[x])
        x+= 8
    
    return questionsList

#return a list of Dicts for the answers
def makeAnswersList(fileName):
    contentsList = getQuestion(fileName)
    answersList =[]
    y =2
    while(y<len(contentsList)):
        answerDict ={}
        for z in range(y+1, y+4):
            answerDict[contentsList[z]] = False
        answerDict[contentsList[y+5]] = True
        answersList.append(answerDict)
        y+= 8
    
    return answersList

    


#openMyFile("test3.txt")    
#tester = getQuestion("test3.txt")
#tester = makeQuestionList("test3.txt")
tester = makeAnswersList("test3.txt")
print(tester)
