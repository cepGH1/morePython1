
fakesMessage = "Incorrect Answers \n"
starter = "Question \n"

def saveMyList1(myList, myList2, myList3, myList4, myList5):
    outputString =""
    for x in range(len(myList)):
        myString = starter
        
        myString += myList[x] +"\n" + fakesMessage + myList2[x] + "\n" + myList3[x] + "\n"+ myList4[x] + "\n"+ " Correct Answer \n" + myList5[x] + "\n"
        outputString += myString
    return outputString
        
def saveMyList2(theString, fileName):
    myFile = open(fileName, "w")
    myFile.write(theString)
    myFile.close
    




