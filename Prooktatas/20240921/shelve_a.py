import shelve

with shelve.open('shelve_data.dat') as s:
    s['name'] = ['Elek', 'Pista', 'Jakab']
    s['language'] = ['Paython', 'JavaScript', 'PHP']
    s['aga'] = [27, 45, 30]

with shelve.open('shelve_data.dat') as s:
    print(s['language'])
    print(s['age'])
    print(s['name'])

with shelve.open('shelve_data.dat') as s:
    for key in s:
        print(key)

with shelve.open('shelve_data.dat', writeback=True) as s:
    key1 = input('Irja be a kulcsot: ')
    num1 = int(input('Hany darab erteket szeretne felvenni: '))
    for i in range(num1):
        val = input('Irja be az erteket: ')
        s[key1].append(val)
    print(s[key1])
    s.sync()


