wuh1 = open("C:\Clare\data\cov19\OL719078_1.txt", "r")
wuh2 = open("C:\Clare\data\cov19\wuhanHu1FullSequence.txt", "r")
print(wuh1)
w1L1 = wuh1.read()
w2L1 = wuh2.read()
print("the length of sequence OL719078_1 is " +str( len(w1L1)))
print("the length of wuhanHu1 is " +str( len(w2L1)))
noEmptyW1 = w1L1.replace(" ", "")
noEmptyW2 = w2L1.replace(" ", "")
w1L1As = noEmptyW1.count("A")
w2L1As = noEmptyW2.count("A")
w1L1Gs = noEmptyW1.count("G")
w2L1Gs = noEmptyW2.count("G")
w1L1Cs = noEmptyW1.count("C")
w2L1Cs = noEmptyW2.count("C")
w1L1Ts = noEmptyW1.count("T")
w2L1Ts = noEmptyW2.count("T")
aRes = "Number of A in cv19 of two different strains are " + str(w1L1As) + " and " + str(w2L1As)
gRes = "Number of Gs in cv19 of two different strains are " + str(w1L1Gs) + " and " + str(w2L1Gs)
cRes = "Number of Cs in cv19 of two different strains are " + str(w1L1Cs) + " and " + str(w2L1Cs)
mytRES = "Number of Ts in cv19 of two different strains are " + str(w1L1Ts) + " and " + str(w2L1Ts)
hk = "\n"
print(aRes)
print(gRes)
print(cRes)
print(mytRES)

#print(noEmptyW1)
#print(w2L1)
wuh1.close
wuh2.close
input1 = input("please enter a file name to store the results")
fileName = "C:/Clare/data/cov19/"  + input1
resultFile = open(fileName, "a")
resultFile.write(hk+aRes+hk+gRes+hk+cRes+hk+mytRES)
resultFile.close

