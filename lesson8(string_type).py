print("It's all right")

print('it\'s all right')

print('I like\'Python\'')

print('he is called "Big Boy"')

text1 = """This is good
life is good
I'am a variable
multiline strings"""

print(text1)

myList = ["Skoda","Nissan","Volvo","Honda"]

print(myList[0])      #list'te ilk eleman 0 sonra birer birer artar

text2 = "Visual Studio Code"

print(text2[0])       #String'de de list gibi ilk eleman 0 dan baslar

print(len(text2))

print("Code" in text2)   #eger bulursa true yazar yoksa false yazar
print("code" in text2)
print("test" in text2)

word1 = "Visual"
print(word1 in text2)

if word1 in text2:
    print("yes! 'Visual' in text2")

word2 = "PyCharm"

if word2 not in text2:
    print("No, 'PyCharm' not in text2")


