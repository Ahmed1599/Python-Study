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

dict = {"name": "Fehmi", "Age": 18}

print(dict)

