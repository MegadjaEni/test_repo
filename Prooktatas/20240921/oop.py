class Madar:
    fajta = 'Tollas allat'

    # példány attributum
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

obj1 = Madar('Csorike', 10)
print(obj1.fajta)
print(obj1.nev)
print(obj1.kor)

print(obj1.__class__.fajta)



class Cirole:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Cirole.pi

    def set_radius(self, new_radius):
        self.area = new_radius
        self.area = new_radius * new_radius * self.pi

    def get_perin(self):
        return self.radius * self.pi * 2


c = Cirole()

print('A szugár: ', c.radius)
print('A terület: ',c.area)
print('A kerület: ', c.get_perin())

c.set_radius(4)

print('A szugár: ', c.radius)
print('A terület: ',c.area)
print('A kerület: ', c.get_perin())




class Madar:

    def __init__(self):
        self.v1 = 'alma'
        self._v2 = 'barack'
        self.__v3 = 'citrom' # private láthatóságnak felel meg, csak osztályon belül
        print('A Madar kész van')

    def fn1(self):
        print('FN1 - Madár')

    def fn2(self):
        print('FN2 - Madár')


class Pingvin(Madar):

    def __init__(self):
        super().__init__()
        print('A Pingvin kész van')

    def fn1(self):
        print('Ez a Pingvin')
        print(self.v1) # public láthatóságnak felel meg, gyermekben és osztályban is látszik
        print(self._v2) # public láthatóságnak felel meg, gyermekben látszik, de kivül nem
        #print(self.__v3) hiba AttributeError: 'Pingvin' object has no attribute '_Pingvin__v3

    def swim(self):
        print('A Pingvin uszik')


p = Pingvin()
p.fn1()
p.fn2()
p.swim()

class Computer:

    def __init__(self):
        self.__max_price = 100000

    def display_price(self):
        print('Az eladási ár: {} Ft'.format(self.__max_price))

    def set_max_price(self, price):
        if price > 100000:
            self.__max_price = price
        else:
            self.__max_price = 200000


c = Computer()
#print(c.__max_price) hiba AttributeError: 'Computer' object has no attribute '__max_price'
c.display_price()
c.set_max_price(1)
c.display_price()