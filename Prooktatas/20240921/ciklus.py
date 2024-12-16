list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in list1:
    if num % 2 == 0:
        print(num)

for letter in "Ez egy mondat":
    print(letter)

tup1 = (1, 2, 3, 4, 5)

for t in tup1:
    print(t)

list1 = [(1, 2), (3, 4), (5, 6)]
for item in list1:
    print(item)

for (t1, t2) in list1:
    print('Eslo: ', t1)
    print('Masodik: ', t2)

d1 = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d1:
    print(item)

for item in d1.items():
    print(item)

for k1, v1 in d1.items():
    print('Kulcs: ', k1)
    print('Ertek: ', v1)

for item in d1.keys():
    print(item)

for item in d1.values():
    print(item)

# 1. bekerjunk a felhasznalotol szamokat (pl.: 15644341874534)
# 2. Deklaralunk egy paros es paratlan listat
# 3. Eldontjuk megyik paros es melyik paratlan
# 4. osszesites (volt, nem volt, es mely szamok - kiiratasnal figyeljuk az egyes vagy tobbes szamra)

numbers = input('Irjon be szamokat:')
odd_list = []
even_list = []

for item in numbers:
    number = int(item)
    if number % 2 == 0:
        if number not in even_list:
            even_list.append(number)
    elif number % 2 != 0 and number not in odd_list:
        odd_list.append(number)
if even_list == []:
    print('Nincs paros szam a bevitelben')
else:
    if len(even_list) == 1:
        print(' A paros szam a kovetkezo:', even_list[0])
    else:
        print('A paros szamok a kovetkezok:', even_list)

if len(odd_list) == 0:
    print('Nincs paratlan szam a bevitelben')
else:
    if len(odd_list) == 1:
        print('A paratlan szam a kovetkezo: ', odd_list[0])
    else:
        print('A paratlen szamok a kovetkezok: ', odd_list)
