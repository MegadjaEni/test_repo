from re import match

first = 5
print(first)
print(first+first)
print(first)
first = 7
print(first)
first= first + first
print(first)

a = 300
b = 0.5
c = a*b
print(c)
print(3//2)
print(8%2)

print("Ez csak egy teszt")
print('Ez csak egy teszt')
#print('ez csak egy teszt") amivel kezded azzal kell befejezni keverni nem lehet
print('elso sor\nMasodik sor')
print("\n")
print("\n")
print('alma')

print(len("Ez csak"))
var1 = "Ez csak"
print(var1)
print(var1[0])
print(var1[1:])
print(var1[3:])
print(var1[:2])
print(var1[:])
print(var1[-1])
print(var1[:-1])
print(var1[::2])
print(var1[::-1])

#var1[0] = 'A' nem változtatható az elem
print(var1 + ' egy teszt')
var1 = var1 + ' egy teszt'
print(var1)
sing = '*'
print(sing * 20)
print(var1.upper())
print(var1)
var1 = var1.upper()
print(var1.lower())
print(var1.split())
print(var1.split('E'))

print('ide beszurok valamit: {}'.format(var1))
print('most ide {} szurtam be valamit'.format(var1))
print('most ide %s szurtam be valamit' %'valami')
print('most ide %s, %s szurtam be valamit' %('alma', 'barack'))
print('most ide \t %s, %s szurtam be valamit' %('alma', 'barack'))
print('A szam %s' %5.25)
print('A szam %d' %5.25)
print('A szam %1.4f' %5.251232444555) #%szam.szamf
print('Elso: %d Masodik: %s Harmadik: %1.2f' %(12, 'alma', 4.5678))
print('Elso: {b} Masodik: {a}'.format(a='alma', b='barack'))
print('*' * 50)
print('{0:8} | {1:9}'.format('Gyumolcs', 'Mennyiség'))
print('{0:8} | {1:9}'.format('Alma', '1kg'))
print('{0:8} | {1:9}'.format('Barack', '2kg'))
print('*' * 50)
print('{0:_<15} | {1:*^15} | {2:->15}'.format('Gyumolcs', 'Mennyiség', 'Bolt'))
print('{0:_<15} | {1:*^15} | {2:->15}'.format('Alma', '1kg', 'Tesco'))
print('{0:_<15} | {1:*^15} | {2:->15}'.format('Barack', '2kg', 'Aldi'))

print(100 > 200)
print(100 < 200)
print(100 == 200)
print(100 == 100)

var2 = 100 > 200
print(var2)

first_list = ['alma', 'barack', 'eper', 42]
print(len(first_list))
print(first_list[0])
print(first_list[:2])
#print(first_list[:2])
#print(first_list['a'])
print(first_list * 2)
print(first_list[-1])
first_list.append('citrom')
print(first_list)
print(first_list.pop())
print(first_list)
first_list.reverse()
print(first_list)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
matrix =[list1, list2, list3]
print(matrix)
print(matrix[0])
print(matrix[2][1])


matrix2 = [
    [
        ['alma', 'barack', 'citrom', 42, 5.2, True],
        ['eper', 'narancs', 'dinnye']
    ],
    [
        ['krumpli', 'zeller', 'repa']
        ]
]
print(matrix2)
print(matrix2[0][1][1])
print(matrix2[1][0][0])

list1.insert(1, 1.5)
print(list1)
list1.clear()
print(list1)
