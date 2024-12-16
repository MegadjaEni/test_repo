#def fugveny_neve(parameterek):
#    """leiras""" #nem kötelező
#    utasitasok

def greeting(name):
    """ez a fgv koszon megszolitva egy embert""" # ez egy doc string
    print("Hello " + name + " Jo reggelt!")

greeting("Elek")
print(greeting.__doc__) # kiírja a fügvény leírását

def even_or_odd(number):
    """Ez a funkcio eldonti egy szamrol, hogy paros vagy paratlan"""
    valami = 'Teszt'
    print(valami)
    if number %2 ==0:
        return "Paros a szam"
    return "Paratlan a szam" # nem feltétlenül kell elis anélkül is jól lefut

print(even_or_odd(3))
print(even_or_odd(4))

