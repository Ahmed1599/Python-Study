## Task 1: Degisken Takasi ve Tip Analizi (Variables & Types)

variable1 = "42"
variable2 = 18.75

variable1,variable2 = variable2,variable1

print(int(variable1), str(variable2))

print("variable1", type(int(variable1)),"    ", "variable2", type(str(variable2)))


## Task 2: Student Card (Formatting & Data Types)

import sys

Name_Surname = input("Enter your name and surname :")
Birth_Year = int(input("Enter your birth year :"))
Height = float(input("enter your height in float (ex = 1.78) :"))


age = 2026 - Birth_Year

height_byte = sys.getsizeof(Height)

print("-----STUDENT CARD-----","\nName :", Name_Surname,"\nAge :", age,"|","Height :", Height,"\nHeight Byte :", height_byte)


# Task 3: agirlikli Piyango cekilisi (Random & Collections)

import random

myList = ["Ali", "Ayse", "Mehmet", "Zeynep", "Can", "Elif"]

three_name_list = random.sample(myList,k=3)

random.shuffle(myList)

print(three_name_list)
print(random.choices(myList,weights=[3,3,3,1,1,1]))


## Task 4: module of complex number (Complex & Math)

z = 3 + 4j

result = (z.real**2 + z.imag**2)**(1/2)

print("Module =", result)

## Task 5: Deterministik Zar Simulasyonu (Random Seed & State)

random.seed(42)

print(random.randint(1,6))
print(random.randint(1,6))
print(random.randint(1,6))

state = random.getstate()

print(random.randint(1,6))
print(random.randint(1,6))

random.setstate(state)

print(random.randint(1,6))
print(random.randint(1,6))


## Task 6: Siber Guvenlik Ajani_Kriptografik Kimlik Dogrulama Motoru

import sys 
import random

name = input("Ajan kod adinizi giriniz: ")
Security_Number = int(input("guvenlik derecesi giriniz (1 to 9): "))

name_byte = sys.getsizeof(name)
Security_Number_Byte = sys.getsizeof(Security_Number)

my_sum = name_byte + Security_Number_Byte

random.seed(Security_Number)

sanal = random.randint(3,8)

comp = complex(Security_Number,sanal)

module = (comp.real**2 + comp.imag**2)**(1/2)

key = random.getrandbits(16)

state = random.getstate()

frekans1 = random.uniform(10.0, 99.9)
print(frekans1)

random.setstate(state)

frekans2 = random.uniform(10.0, 99.9)
print(frekans2)

symbols = ["Alpha", "Beta", "Gamma", "Delta", "Omega", "Sigma"]

two_code_name = random.sample(symbols,k=2)

one_characters = random.choices(symbols,weights=[1, 1, 2, 2, 5, 10])

random.shuffle(symbols)

if frekans1 == frekans2:
    print(
        "================ AJAN DOGRULAMA RAPORU ================",
        "\n Ajan:", name, "|", "Guvenlik:", Security_Number,
        "\n Sistem Bellek Yuku:", my_sum, "Byte",
        "\n Kuantum koordinat modulu:", module,
        "\n16-Bit oturum anahtari:", key,
        "\nDogrulanmis Frekans:", frekans1,
        "\nAtanan Kodlar:", two_code_name,
        "\nAna Protokol:", one_characters,
        "\n======================================================",
    )
else:
    print("Hata!!!Frekanslar eslesmedi!!!")