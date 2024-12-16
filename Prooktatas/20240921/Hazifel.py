from copyreg import pickle
from os.path import dirname

from pandas.io.formats.printing import PrettyDict


def calculate_sphere_volume(r):
    terfogat = (4 / 3) * 3.14 * (r ** 3)
    return terfogat
sugar = 6
terfogat = calculate_sphere_volume(sugar)
print(f"A gömb sugara {sugar} centimeter a terfogata: {terfogat:.2f} cm³")


def square(num):
    return num * num
def square(num):
    return num * num
square2 = lambda num: num * num # beszorozza önmagával a számot
add = lambda a,b: a + b # össze adja
ad = lambda a,b: b*a

print(square2(10))
print(add(3,2))
print(ad(15,5))
print(add.__name__)


import os


print(os.walk('zene'))
for item in os.walk('zene'):
    print(item)
for utvonal, konyvtarak, fajlok in os.walk('zene', topdown= True):
    print(utvonal)
    slpit1 = os.path.split(utvonal)
    print(slpit1)
    slpit2 = os.path.split(slpit1[0])
    for f in fajlok:
        print(f[:-5].split('Pink Floyd'))







