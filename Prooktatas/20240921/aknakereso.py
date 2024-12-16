import random
import os
from colorama import init, Fore, Style
init(autoreset=True)

tabla_size = 10
num_aknak = 10

def create_tabla():
    """
    Létrehozza a játéktáblát, aknákkal elhelyezve, de nem jeleníti meg az aknákat.
    """
    tabla = [[' ' for _ in range(tabla_size)] for _ in range(tabla_size)]
    aknak = set()

    while len(aknak) < num_aknak:
        x = random.randint(0, tabla_size - 1)
        y = random.randint(0, tabla_size - 1)
        aknak.add((x, y))

    for (x, y) in aknak:
        tabla[x][y] = 'X'
    return tabla, aknak

def count_adjacent_mines(x, y, aknak):
    """
    Számolja meg hány akna található a mező körül.
    """
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < tabla_size and 0 <= ny < tabla_size and (nx, ny) in aknak:
            count += 1
    return count

def reveal(x, y, tabla, aknak, felfedett):
    """
    Felfedi a mezőket, ha azok biztonságosak.
    Ha nincs körülötte akna, akkor tovább felfedi a szomszédos mezőket.
    """
    if (x, y) in felfedett:
        return
    adjacent_mines = count_adjacent_mines(x, y, aknak)

    if adjacent_mines == 0:
        tabla[x][y] = ' '
    else:
        tabla[x][y] = str(adjacent_mines)
    felfedett.add((x, y))

    if adjacent_mines == 0:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < tabla_size and 0 <= ny < tabla_size and (nx, ny) not in felfedett:
                reveal(nx, ny, tabla, aknak, felfedett)

def print_tabla(tabla, felfedett, aknak, szinezett_elem):
    """
    Kiírja a táblát a konzolra, de az aknák nem látszódnak, csak a felfedezett mezők.
    """
    os.system('cls')

    print("    ", end="")
    for i in range(tabla_size):
        print(f"{i:2}", end=" ")
    print()

    for i, row in enumerate(tabla):
        print(f"{i:2} |", end=" ")
        for j, cell in enumerate(row):
            if (i, j) in felfedett:
                adjacent_mines = count_adjacent_mines(i, j, aknak)
                if adjacent_mines == 0:
                    if (i, j) in szinezett_elem:
                        print(Fore.GREEN + ' O' + Style.RESET_ALL, end=" ")
                    else:
                        print(' O', end=" ")
                else:
                    if (i, j) in szinezett_elem:
                        print(Fore.RED + f" {adjacent_mines} " + Style.RESET_ALL, end=" ")
                    else:
                        print(f" {adjacent_mines} ", end=" ")
            else:
                print(' .', end=" ")
        print()
        if i < tabla_size - 1:
            print("    +" + "---+" * (tabla_size - 1))

def play_game():
    """
    Játékmenet, ahol a játékos megpróbálja elkerülni az aknákat.
    """
    tabla, aknak = create_tabla()
    felfedett = set()
    szinezett_elem = set()
    print("Üdvözöllek az aknakereső játékban!")
    print(f"A játéktábla mérete: {tabla_size} x {tabla_size}")
    print(f"Akmák száma a játékban: {num_aknak}")
    print("A koordinátákat 0 és 9 között lehet, sor és oszlop!")
    step = tabla_size * tabla_size - num_aknak

    while step > 0:
        print_tabla(tabla, felfedett, aknak, szinezett_elem)

        try:
            x, y = map(int, input(f"Adja meg a koordinátákat (x, y): ").split())
        except ValueError:
            print("Rossz koordinátákat adott meg!")
            continue

        if not (0 <= x < tabla_size and 0 <= y < tabla_size):
            print('Érvénytelen, próbálja újra!')
            continue

        if (x, y) in aknak:
            print("Aknát találtál! Vesztettél.")
            break
        else:
            reveal(x, y, tabla, aknak, felfedett)
            szinezett_elem.add((x, y))
            step -= 1
            print(f"{step} lépés maradt.")

        if step == 0:
            print("Gratulálok, nyertél!!")

if __name__ == "__main__":
    play_game()



