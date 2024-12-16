import random

def racs_keszitese(size):
    return [[' ' for i in range(size)] for i in range(size)]

def racs_megjelenites(racs):
    for sor in racs:
        print(' '.join(sor))

def szo_elhelyezes(racs, szo):
    meret = len(racs)
    szo_hossz = len(szo)

    elhelyezve = False
    while not elhelyezve:
        irany = random.choice(['sorok', 'oszlopok'])
        if irany == 'sorok':
            sor = random.randint(0, meret - 1)
            oszlop = random.randint(0, meret - szo_hossz)
            if all(racs[sor][oszlop + i] == ' ' for i in range(szo_hossz)):
                for i in range(szo_hossz):
                    racs[sor][oszlop + i] = szo[i]
                elhelyezve = True

        else:
            sor = random.randint(0, meret - szo_hossz)
            oszlop = random.randint(0, meret - 1)
            if all(racs[sor + i][oszlop] == ' ' for i in range(szo_hossz)):
                for i in range(szo_hossz):
                    racs[sor + i][oszlop] = szo[i]
                elhelyezve = True

def racs_kitoltes(racs):
    abc = 'QWERTZUIOPŐÚÖÜÓASDFGHJKLÉÁŰÍYXCVBNM'
    for sor in range(len(racs)):
        for oszlop in range(len(racs[sor])):
            if racs[sor][oszlop] == ' ':
                racs[sor][oszlop] = random.choice(abc)

def main():
    szavak = ["ALMA", "DINNYE", "EPER", "BANÁN", "KIWI", "SZILVA", 'CITROM', "AVOKADÓ", "MÁLNA", "MEGGY"]
    meret = 10
    racs = racs_keszitese(meret)

    for szo in szavak:
        szo_elhelyezes(racs, szo)

    racs_kitoltes(racs)
    racs_megjelenites(racs)

print("\n10 db szót kell megtalálnod! Sok sikert")

if __name__ == "__main__":
    main()