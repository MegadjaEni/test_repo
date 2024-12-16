try:
    f = open('tesztfile', "w")
    f.write('Írjuk ezt bele')
except IOError:
    print('Hiba: Nem találhatom a fájlt, vagy nincs hozzá jogom!')
except:
    print('Kritikus hiba történt!')
else:
    print('Tartalom sikeresen kiírva!')
    f.close()
finally:
    print('Minden esetben lefut')
