import json

data = {}
data['tanulok'] = []
data['tanulok'].append({
    'nev': 'Mekk Elek',
    'kedvenctantargy': 'Fizika',
    'szuletesihely': 'Budapest'
})
data['tanulok'].append({
    'nev': 'Teszt Elek',
    'kedvenctantargy': 'Tesi',
    'szuletesihely': 'Debrecen'
})
data['tanulok'].append({
    'nev': 'Gipsz Jakab',
    'kedvenctantargy': 'Matek',
    'szuletesihely': 'Miskolc'
})

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)
    #print(json.dumps(data))

with open('data.json', 'r', encoding='utf-8') as file:
    json_value = json.load(file)
    #print(json_value)
   for item in data['tanulok']:
       print('Neve: ' + item['nev'])
       print('Kedvenc tantargy: ' + item['kedvenctantargy'])
       print('Szuletesi hely: ' + item['szuletesihely'])
