dic1 = {'key1': 'alma', 'key2': 'barack'}
print(dic1)
print(dic1['key2'])
dic1 = {'key1': 123, 'key2': [12, 22, 33], 'key3': ['elem1', 'elem2', 'elem3']}
print(dic1)
print(dic1['key3'][1])
print(dic1['key3'][1].upper())
print('elem2'.upper())
dic1['key1'] = dic1['key1'] - 123
print(dic1['key1'])
dic1['key1']-= 123
print(dic1['key1'])

dic2 = {}
print(dic2)
dic2['k1']= 'Alma'
dic2['k2'] = "Eper"
print(dic2)

dic_matrix = {
    'key1': {
        'subkey1': {
            'subsubkey1': ['alma', 'barack']
        }
    }
}
print(dic_matrix['key1']['subkey1']['subsubkey1'][1])

dic4 = {'key1': 1, 'key2': '2', 'key3': 3}
print(dic4.keys())
print(dic4.values())
print(dic4.items())
print(dic4['key3'])
print(dic4.get('key3'))
#print(dic4['key4']) #KeyError: 'key4'
print(dic4.get('key4')) #None
#print(dic4.pop())
print(dic4.popitem())
print(dic4.get('key4', 'Fapapucs'))

dict5 = {}
dict5.update(dic1)
dict5.update(dic2)
dict5.update(dic4)
print(dict5)

shopping_dic = {'alma': 1, 'barack': 2, 'cukor': 2, 'eper': 4, 'dinnye':5}
var1= input('keren adja meg mire kivancsi:')
print(shopping_dic.get(var1.lower(), 'Ilyen tetelt nem akar vasarolni'))







