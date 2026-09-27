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