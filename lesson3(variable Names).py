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