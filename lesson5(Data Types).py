#Data Types

name = "Ahmet" #string - str
age = 18       #integer - int
weight = 77.5  #float
comp= 2j       #complex (karmasik sayilar)

print("name: " + name + " age: " + str(age) + " weight: " + str(weight) + " Complex: " + str(comp))

myList = ["Apple","Grape","Cherry","Banana","Lemon"]      #list data type

print(type(myList))
print(myList)

myTuple = ("Apple","Grape","Cherry","Banana","Lemon")     #Tuple(demet) data type
print(type(myTuple))
print(myTuple)


myRange = range(10)  #Range Data type               #Range turu sifirdan icine yazdiigmiz sayinin bir eksigine kadar yazar 

print(type(myRange))
print(myRange)

myDict = {"Name":"Ahmet", "Age":18}                 #Dictionary data type

print(type(myDict))
print(myDict)

mySet = {"Apple","Grape","Cherry","Banana","Lemon"}  #Set data type

print(type(mySet))
print(mySet)

myFrozen = frozenset({"Apple","Grape","Cherry","Banana","Lemon"})    #Frozenset data type

print(type(myFrozen))
print(myFrozen)

myBool = True             #Bool data type

print(type(myBool))
print(myBool)

NoneType = None    #NONE type (veriable in henuz bos oldugunu belirtir)

print(type(NoneType))
print(NoneType)

import sys

number = 17

print(sys.getsizeof(number))



x = 15
y = 14.53
z = 3j

print("int=",x,", Float=",y,", comlex=",z)

print("\nint=",x,"\nFloat=",y,"\ncomlex=",z)

t = 21E4  #E harfi 10 u temsil eder ondan sonraki harfte 10un ussunu temsil eder

print(t)