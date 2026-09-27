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