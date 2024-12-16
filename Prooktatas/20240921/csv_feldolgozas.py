import csv
from dataclasses import field
from wsgiref.validate import header_re

with open('./test.csv') as file:
    content = csv.reader(file)
    print(content)
    for line in content:
        print(line)

with open('./test.csv2') as file:
    content = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONE)
    print(content)
    for line in content:
        print(line)

csv.register_dialect('dialect1', delimiter=';', quoting=csv.QUOTE_NONE)

with open('./test.csv2', 'r', encoding='utf-8') as file:
    content = csv.reader(file, dialect="dialect1")
    for line in content:
        print(line)

data = [
    [1,2,3, 'cica'],
    ['Alma', 'Barack', 'citrom', 'Cseresznye', 'Eper']
]

file = open('./test.csv3', 'w', encoding='utf-8', newline='')
with file:
    content = csv.writer(file, dialect='dialect1')
    content.writerows(data)

with open('./test.csv3', 'r', encoding='utf-8', newline='') as file:
    content = csv.reader(file, dialect='dialect1')
    next(content)
    for item in content:
        print(f"{item[0]} - {item[1]}")

with open('./test.csv3', 'r', encoding='utf-8', newline='') as file:
    content = csv.reader(file, dialect='dialect1')
    print(content)
    data = list(content)
    print(data)

with open('./cicak.csv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file, dialect='dialect1')
    csv_writer.writerow(['Nev', 'Kor'])
    csv_writer.writerow(['Potyi', '1'])
    csv_writer.writerow(['Bogyo', '2'])

with open('./cicak.csv', 'w', encoding='utf-8', newline='') as file:
    header = ['Nev', 'Fajta', 'Kor']
#    dict_writer = csv.DictWriter(file, fieldnames=header, dialect='dialest1')
#    dict_writer.writeheader()
#    dict_writer.writerow({
#        "Nev": "Bogyo",
#        "Fajta": "Hazi cica",
#        "kor": 5,
#    })
#with open('./cicak.csv', 'r', encoding='utf-8', newline='') as file:
#    dic_reader = csv.DictWriter(file, dialect='dialect1')
#    for line in dic_reader:
#        print(line['Nev'])


