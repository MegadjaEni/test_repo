# palindrom feladat
#1. Be kell kernia szót
#2. kisbetusitjuk amit beirt
#3. osszehasonlitjuk a szot megforditva onmagaval

word = input('Kerem adjon meg egy szot: ')
word = word.lower()

if word == word[::-1]:
    print('A szo egy palindrom szo')
else:
    print('A beirt szo nem palindrom')

list1 = list(word)
list2 = list(word)
list2.reverse()

if list1 == list2:
    print('A szo egy palindrom')
else:
    print('A beirt szo nem palindrom')
