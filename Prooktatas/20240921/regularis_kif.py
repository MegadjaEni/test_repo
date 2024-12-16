import re

sentence = "Elemezzuk ki ezt a mondatot pythonban"

m = re.match(r'(.*) ki (.*)', sentence, re.M | re.I) #re.M => ^$

if m:
    print('Van talalat')
    print(m.group()) #vissza adja mind ket csoportot
    print(m.group(1))
    print(m.group(2))
else:
    print('Nincs talalat')

sentence = 'Szeretem a Pythont'
m = re.search(r'(pythont)', sentence, re.I)
if m:
    print("van talalat")
    print(m.group())
else:
    print('Nincs talalat a search fgv-l')

m = re.match(r'(pythont)', sentence, re.I | re.M)
if m:
        print("van talalat")
        print(m.group())
else:
        print('Nincs talalat a match fgv-l')

email = 'info@tesezt_toroldt.hu'

#m = re.match('ezt_torold', email)
m = re.search('ezt_torold', email)

if m:
    print('Eamil cim: ', email[:m.start()] + email[m.end():])
else:
    print('Nincs talalat')

phone = 'Kerem hivja ezt a szamot # +36-70 123-4567'
phone_number = re.sub(r'\D', '', phone)
print('A nyes szam: ',phone_number)

var2 = 'Alama, Barack, Banan'
m = re.split(r'\W+', var2)
if m:
    print(m)
else:
    print('Nincs talalat')


import math
print(math.ceil(14.15)) #felkerekítés
print(math.sqrt(100)) #gyök vonás





