# fajlt be kell olvasni
# a számokat tartalmazó öt oszlopot kigyűjteni a feldolgozás végett (öt lista az oszlopokkal)
# megkell számolni az előfordulásokat
# ki kell irni az öt leggyakoribbat
import csv
from typing_extensions import Counter

csv.register_dialect('lotto_dialektus', delimiter=';', quoting=csv.QUOTE_NONE)
with open('otos.csv', encoding='utf-8', newline='') as file:
    reader = csv.reader(file, dialect='lotto_dialektus')
    winning_numbers1 = []
    winning_numbers2 = []
    winning_numbers3 = []
    winning_numbers4 = []
    winning_numbers5= []
    for row in reader:
        winning_numbers1.append(row[-5])
        winning_numbers2.append(row[-4])
        winning_numbers3.append(row[-3])
        winning_numbers4.append(row[-2])
        winning_numbers5.append(row[-1])

n1 = Counter(winning_numbers1)
n2 = Counter(winning_numbers2)
n3 = Counter(winning_numbers3)
n4 = Counter(winning_numbers4)
n5 = Counter(winning_numbers5)
print(n1.most_common(1)[0][0] + ', ' + n2.most_common(1)[0][0] + ', ' + n3.most_common(1)[0][0] + ', ' + n4.most_common(1)[0][0] + ', ' + n5.most_common(1)[0][0] + ', ')



