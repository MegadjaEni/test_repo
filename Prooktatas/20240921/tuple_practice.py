t1 = (1, 2, 3)
t2 = (1,)
print(len(t1))
t3 = ('Elso', 2)
print(t3)
print(t3[0])
print(t3[-1])
print(t3.index('Elso'))#keresés
print(t3.count('Elso'))
#t3.append('Elem') #AttributeError: 'tuple' object has no attribute 'append' #nem lehet hozzá adni
#t3[0] = 'Alma' #TypeError: 'tuple' object does not support item assignment #nem lehet megváltoztatni

t4 = (['alma', 'barack'], ['citrom', 'eper'])
print(t4)
t4[0].append('dinnye')
print(t4)

t5 = t1 + t2 + t3 + t4
print(t5)
