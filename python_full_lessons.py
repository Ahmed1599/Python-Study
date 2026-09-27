## LESSON 1 PRINT

print("I Want to learn Python")

if 5 + 4 == 7:
    print("True answer")

#This is a comment

#Coklu yorum satiri olmadigi icin atanmamis string kullanilabilir

'''
I like python
Because I want to be
a computer engineer
'''

#birden fazla satira ayni anda yorum isareti eklemek icin (CTRL + K)+(CTRL + C) kisayolu kullanilir.

## LESSON 2 VARIABLES

#Variables

x = 10   #integer
a = str(10)

y = 1.5  #float
b = int(1.5)

z = "python"  #string

print(x)
print(y)
print(z)

#type fonksiyonu ile turu belirlenir

print(type(x))
print(type(y))
print(type(z))

print(a)
print(type(a))

print(b)
print(type(b))

#python buyuk kucuk harflere duyarlidir
#ayni harften bir buyuk bir kucuk bir degisken yaptigimizda ikisi farkli olur

abc = "kucuk" 

ABC = "buyuk"

print(abc)

print(ABC)

## LESSON 3 VARIABLE NAMES

#bir variable sayi ile baslayamaz. sadece harf veya alt cizgi ile baslar
#bir variable adi sadece harfler sayilar ve alt tire (_) bulundurabilir

name1 = "Ahmet"
_surname1 = "Rihavi"

print(name1)
print(_surname1)

#yazimi kolaylastirma amaciyla birlesik kelimeleri ilk kelime haric her kelimeyi buyuk harfle baslanir (camelCase)
#ya da hepsi buyuk harfle baslar (PascalCase)
#ya da her kelimelerin arasina alt tire konulur (snake_case)

#variable ayni satirda virgulle ayrilarak ve sonra esittirden sonra da olan degerler virgulle ayrilirsa python bunlari sirayla eslestirir

x, y, z = "Banana", "Apple", "Grape" 

print(x)
print(y)
print(z)

#birden fazla degiskene ayni degeri vereceksek hepsini tek tek yazmak yerine yan yana yazip aralarina esittir(=) koyup en sonda istedigimiz degere esitleriz

a = b = c = "white"

print(a)
print(b)
print(c)

name = "Ahmed"
name2 = name

print(name2)

## LESSON 4 OUTOUT VARIABLES

#birden fazla variable in beraber ciktisini almak icin ya virgul ya da toplama kullanilir.
#virgul kullanildigi durumda python araya bosluk koyar

a = "Welcome"
b = "to Python"
c = "lessons"

print(a, b, c)

#toplama isareti kullandigimizda ise bosluklari kelime sonlarina bizim koymamiz gerekir

print(a + b + c)

d = "Welcome "
e = "to Python "
f = "lessons"

print(d + e + f)

#degiskenlerin biri string biri integer olursa bunlari virgulle yan yana yazdirabiliriz
#eger bunlari toplamayla duz haliyle toplamaya kalkarsak python hata verir

g = 10
h = 1.5
print(g, f)

#Turler birbirinden farkli oldugunda toplama ile yan yana yazilamazken sadece float ve integer toplanir.

print(g + h)

#donusturme fonksiyonlariyla degiskenleri ayni tipe ayarlarsak toplama kullanilabilir
#integer stringe donusur, float integer ve stringe donusur; ancak string yalnizca sayi iceriyorsa int/float tipine donusebilir

print(str(g) + f)
print(str(h) + str(g) + f)

#Global variables
#def kismi sonra ogretilecek simdilik sadece global function icin kullanildi
#def ten sonra fonksiyon tanimlanirken def altindaki degistirilen degiskenin onceki satirina (global [Degisken ismi]) yazilmazsa 
# o degistirilen veya uretilen degisken function disi kullanilamaz

x = "marvellous"
y = "fantastic"

def myFunction():
    global text1
    text1 = "fantastic"
    y = "marvellus"
    print("Python is " + y)

myFunction()

print(x)
print(text1)
print(y)

#variable lar kodun ilerilerinde degisebilir

number = 7 
print(number)

number = 25
print(number)

number = number + 2

print(number)

number1 = complex(2+3j)
number2 = complex(2,3)
number3 = complex(2 - 3j)

print(number1)
print(number2)
print(number3)

Car = ("mercedes", "BMW", "Ferrari", "Lamborghini")

print(list(Car))
print(tuple(Car))
print(set(Car))
print(frozenset(Car))

my_dict = {"name": "Fehmi", "Age": 18}

print(my_dict)

## LESSON 5 DATA TYPES

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

## PRACTICE 1 DAIRE ALAN CEVRE

pi = 3.14159

r = float(input("Daire yaricapini giriniz:"))

daire_alani = pi*r*r
daire_cevresi = 2*pi*r

print("Dairenin Alani =", daire_alani, ", Dairenin cevresi =",daire_cevresi)

## LESSON 6 RANDOM

import random

#Random modulu zamana bagli olarak rastgele sayi secen bir moduldur.

print(random.random())

random.seed(7)              #Seed, Random modulunun zamana bagli degisen secimini belirli bir sayiyla sabitler
print(random.random())
print(random.random())

random.seed(None)

print(" \n ")

print(random.random())

state = random.getstate()    #getstate, bir sonraki random ciktisinin degerini esitlenen variable'a atar
print(random.random())

random.setstate(state)       #setstate, getstate'nin atadigi degeri bir sonraki randoma uygulamak amaciyla kullanir
print(random.random())

print(random.random())

print(random.getrandbits(18))   #getraindbits, ikilik sistemde (binary) $k$ basamakli rastgele bir sayi uretir; 
#                               #yani (0) ile (2^k - 1) arasinda (her ikisi de dahil) rastgele bir tam sayi secer

print(random.randrange(1,10))  #randrange, yazilan araligin icinden sayi secer, 1. sayiyi dahil ederken 2. sayiyi dahil etmez

print(random.randrange(11,22,3)) #3. bir sayi daha girilirse artis miktari olarak alinir or: 11,14,17,20

print(random.randint(1,10))   #randrange ile aynidir tek farki 2. sayiyida dahil eder ve 3. parametre almaz

# print(random.randint(1,10,2))           python hata verir

myList = ["Apple","Grape","Cherry","Banana","Lemon"]

print(random.choice(myList))   #choice, verilen belirli bir data type icinde bulunan ogelerden birini rastgele yazar

text = "Python"
print(random.choice(text))

print(random.choices(myList,weights=[5,4,3,2,1]))  #Choices, listeden verdigimiz sayilari sirayla degerlerle eslestirerek
#                                                  #bu degerlerden sayilarla dogru orantili olarak birini secer

print(random.choices(myList,weights=[1,2,3,4,5],k=18)) #ucuncu parametre olarak k yi girersek kac sayi istedigimizi belirtiriz

random.shuffle(myList)       #shuffle, verilen degistirilebilir veri tiplerinin sirasini karma olarak verir

print(myList)

print(random.sample(myList,k=3))    #sample,veri turunden 2. parametrede verilen deger kadar degeri ceker

print(random.sample(text,k=3))    #shuffle sadece degistirilebilir veri tipinde calisirken sample tumunde calisir

print(random.uniform(25,50))      #uniform, verilen iki sayi arasindan rastgele bir ondalikli sayi ceker

print(random.triangular(25,50))   #triangular uniform'dan  tek farki vardir o da 3. bir parametre belirterek hangi sayiya
#                                 #daha yakin olmasini istedigimizi belirtebiliriz, 2 parametre olursa uniformun gibi calisir

print(random.triangular(25,50,28))

## LESSON 7 RANDOM STATICS HARD (tekrara gerek yok sadece oylesine)

import random

print(random.betavariate(1,100))   #Betavariate 0 ile 1 arasindan rastgele bir ondalikli sayi alir
print(random.betavariate(1000,2))  #1. sayi buyurse sonuc 1 e yaklasir, 2. sayi buyurse 0 a yaklasir.(tersi gecerlidir)
print(random.betavariate(1, 0.0001))

print(random.expovariate(0.5))    


print(random.gammavariate(100,2))

print(random.gauss(100,50))

print(random.lognormvariate(0.2,0.8))

print(random.normalvariate(40,120))

print(random.vonmisesvariate(0,5))

print(random.paretovariate(5))

print(random.weibullvariate(1,2.5))