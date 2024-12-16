class SimpleClass:
    class_variable = "Ez egy osztály változó"

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def class_method(cls):
        print(f'Class method hozzá fér az osztályhoz: {cls.class_variable}')

    @classmethod
    def change_class_variable(cls, new_value):
        cls.class_variable = new_value


obj = SimpleClass('Példány érték')

obj.class_method()

SimpleClass.change_class_variable('Új osztályváltozó értéke')

obj.class_method()


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split(', ')
        return cls(name, int(age))


person = Person.from_string('Teszt Elek, 30')
print(person.name)
print(person.age)
