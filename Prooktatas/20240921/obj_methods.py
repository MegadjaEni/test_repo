class MyClass:
    def __str__(self):
        return 'Ez egy user friendly szöveg'


obj = MyClass()
print(obj)
print(str(obj))

print(repr(obj))

class MyClass2:
    def __repr__(self):
        return 'Ez egy user friendly szöveg2'

obj2 = MyClass2()
print(obj2)

class MyClass3:

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return f'Ez egy új uf szöveg: {self.v1} és {self.v2}'

    def __repr__(self):
        return "MyClass2(v1='első érték', v2='Második érték')"

obj3 = MyClass3('alma', 'Barack')

print(obj3)
print(str(obj3))
print(repr(obj3))


class DClass:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

obj4 = DClass('alma', 'citrom')

print(obj4.__dict__)
print(obj3.__dict__)