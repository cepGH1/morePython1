

print ( "hello world")
if 5>4:
    print("yes")

catName1 = "Zan"
catName2 = "Leia"
print(catName1 + " " + catName2)
print(catName1[1:2])
print(catName2.upper())

a = "can,ven,fin,car"
print(a.split(","))
b = a.split(",")
print(b[0])
print(type(b))
print("Once upon a time \n In a galaxy far far away")

def myFirstFunction():
    print("this functions prints")

myFirstFunction()
 
from Owl import MyOwl


vam = MyOwl("fiona")
print(vam.name)

import datetime

x = datetime.datetime.now()
print(x) 