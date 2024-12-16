# 1. Behúzás
from tkinter.constants import FIRST

from sqlalchemy.dialects.postgresql.base import PGCompiler


def f1():
    a = 10
    if a > 10:
        print('Nagyobb')

# 2. Sorhossz
def ez_egy_hosszu_fn_lesz(elso_parameter, masodik_parameter,
                          harmadik_parameter, nagyedik_parameter,
                          otodik_parameter, hatodik_parameter):
    pass

user_age = 40
userAge = 40

a = 40
b = 20
c = 10

a = b * c

def fn1(a):
    if a > 0:
        return True
    return False

sum = (a * b) + \
       (b * c)


def fn2():
    import os
    pass

var1 = True

if var1 == True:
    print('True')
if var1 == False:
    print('Fale')
if var1 == None:
    print('None')

if var1:
    print('True')
if not var1:
    print('Fale/None')


def double(x):
    return x * 2

daub = lambda x: x * 2


lst1 = [1, 2, 3]
dic1 = {'key': 'Value'}

name = 'Elek'
age = 20

v1 = "Szia," + name + ". A korod" + str(age) + " eves."
v2 = f"Szia, {name}. A korod {age} eves."
v3 = f"Szia, . A korod  eves.".format(name, age)


if var1: print(double(3))

if var1 and v1 and age == 10 and name == 'Elek': print(double(3))

if var1 and v1 and age == 10 and name == 'Elek':
    print(double(3))

FIRST_CONST = 5
if var1 and v1 and age == 10 and \
        name == 'Elek': # a \ az sortörés
    print(double(3))

elso     = 1
masodik  = 2 # több változó eseténél az =-séget össze kell igazítani
harmadik = 3
negyedik = 4
otodik   = 5

# ellenőrzi, hogy a kor eléri-e a 20-at
if age >= 20:
    print('OK')