# 1. szokészlet létehozása
# 2. szórács létrehozása
# 3. szavak elhelyezése a szórácsban különböző irányban
# 4. üres cellákat véletlen szerű betűkkel kitölteni
# 5. számozott rács megjeleítése
# 6. felhasználói input a koordinátákhoz
# 7. szavak megjelölése a rácsban (ha megtalálták)
# 8. fő játékmenet
import random
from colorama import init, Fore, Style


init(autoreset=True)


def get_word_list() -> list[str]:
    """
    A játék szókészlete

    Args:
        None

    Returns:
        Egy lista szavakkal
    """
    return ['PYTHON', 'HTML', 'CSS', 'PROGRAM', 'LOGIKA', 'NOTEBOOK', 'SZINTAXIS']


def create_empty_grid(size=10):
    """
    Üres rács létrehozása

    Parameters:
        - size (int): A rács mérete

    Returns:
        - Az üres rács
    """
    return [[' ' for _ in range(size)] for _ in range(size)]

def place_word_in_grid(grid, word):
    """
    Szó a rácsba helyezése
    Args:
        grid(list): A szórács
        word(str): A szó
    Returns:
        None
    """
    size = len(grid)
    directions = ['horizontal', 'vertical', 'diagonal']
    placed = False

    while not placed:
        direction = random.choice(directions)
        start_row, start_col = random.randint(0, size -1), random.randint(0, size -1)

        if direction == 'horizontal' and start_col + len(word) <= size:
            for i in range(len(word)):
                grid[start_row][start_col + i] = word[i]
            placed = True
        elif direction == 'vertical' and start_row + len(word) <= size:
            for i in range(len(word)):
                grid[start_row + i][start_col] = word[i]
            placed = True
        elif direction == 'diagonal' and start_row + len(word) <= size and start_col + len(word) <= size:
            for i in range(len(word)):
                grid[start_row +i][start_col + i] = word[i]
            placed = True


def fill_empty_cells(grid):
    """
    A rács üres celláinak a feltöltése rendom betűkkel
    Args:
        grid(list): A rácss
    Returns:
        None
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ' ':
                grid[row][col] = chr(random.randint(65,90))


def display_grid(grid):
    """
    A számozott rács megjelenítése

    Args:
        grid(list): A rácss
    Returns:
        None
    """
    print("\nJátékrács (sor- és oszlopszámokkal):")
    header = "  " + " ".join(f"{i}" for i in range(len(grid)))
    print(header)
    print(" " + "--" * len(grid))
    for idx, row in enumerate(grid):
        print(f"{idx} | " + " ".join(f"{Fore.GREEN}{cell}{Style.RESET_ALL}" if cell.islower() else cell for cell in row))


def get_word_selection() -> tuple[int]:
    """
    Felhasználói input kezelése

    Args:
        None
    Returns:
        Koordináták
    """
    print('\nSegítség a koordináták megadásához: ')
    print("- Sor és oszlop számát adja meg (pl.: kezdő sor: 2, oszlop: 3)")
    print("- Végpontként adja meg a végső sor és oszlop számát (pl.: vég sor 2, oszlop:7)")
    print("Példa a 'SZINTAXIS' szóhoz a kezdő koordináták (1,1), vég koordináták (1,8)")

    start_row = get_number_input('Adja meg a szó kezdősornak a számát (0-9): ')
    start_col = get_number_input('Adja meg a szó kezdőoszlopának számát (0-9): ')
    end_row = get_number_input('Adja meg a szó végsorának a számát (0-9): ')
    end_col = get_number_input('Adja meg a szó végoszlopának a számát (0-9): ')
    return start_row, start_col, end_row, end_col


def get_number_input(user_str: str) -> int:
    """
    Felhasználói input kezelése,mely csak számot fogad el

    Args:
        user_str (str): A user input szövege

    Returns:
        A kiválasztott koordináta
    """
    while True:
        input_str = input(user_str)
        if input_str.isdigit() and 0 <= int(input_str) <= 9:
            return int(input_str)

def check_and_nark_word_in_grid(grid, word, start_row, start_col, end_row, end_col):
    """
    A szó ellenörzése a rácsba, ga megvan

    Args:
        grid (list): A rács
        word (str): A szó
        start_row (int): A kezdősor koordinátája
        start_col (int): A kezdő oszlop koordinátája
        end_row (int): A végpont sorának a koordinátája
        end_col (int): A végpont oszlopának a koordinátája

    Returns:
        (boolean): Megvan-e
    """
    word_length = len(word)
    # Vizszintes ellenörzés es megjelölés
    if start_row == end_row:
        if abs(start_col - end_col) +1 == word_length:
            for i in range(word_length):
                if grid[start_row][min(start_col, end_col)+ i] != word[i]:
                    return False
                # Ha megvan jelöljük ki a szót kisbetükkel és szinezéssel
                for i in range(word_length):
                    grid[start_row][min(start_col, end_col) + i] = grid[start_row][min(start_col, end_col) + i].lower()
                return True
    # Függőleges ellenörzés és megjelölés
    elif start_col == end_col:
        if abs(start_row - end_row) + 1 == word_length:
            for i in range(word_length):
                if grid[min(start_row, end_row) + i][start_col] != word[i]:
                    return False
                for i in range(word_length):
                    grid[min(start_row, end_row) + i][start_col] = grid[min(start_row, end_row) + i][start_col].lower()
                    return True
    # Átlos ellenörzés
    elif abs(start_row - end_row) + 1 == word_length and abs(start_col - end_col) +1 == word_length:
        for i in range(word_length):
            if grid[start_row + i][start_col + i] != word[i]:
                return False
            for i in range(word_length):
                grid[start_row + i][start_col + i] = grid[start_row + i][start_col + i].lower()
            return True
        return  False


def main():
    grid = create_empty_grid()
    word_list = get_word_list()
    place_word = []

    for word in word_list:
        place_word_in_grid(grid, word)
        place_word.append(word)

    fill_empty_cells(grid)
    display_grid(grid)
    print("\nA rejtett szavak: ", ', '.join(word_list))

    found_words = []

    while len(found_words) < len(word_list):
        print('\nTalált szavak: ', ", ".join(found_words))
        selection = get_word_selection()

        if selection in None:
            continue # hibás input

        start_row, start_col, end_row, end_col = selection

        found =  False
        for word in word_list:
            if word not in found_words and check_and_nark_word_in_grid(grid, word, start_row, start_col, end_row, end_col):
                print(f"Megtaláltad a következő szót: {word}")
                found_words.append(word)
                found = True
                break

        if not found:
            print("Nincs szó a megadott helyen, próbálja újra!")

        display_grid(grid)

    print('\nGratulálunk! Megtaláltad az összes szót!')

main()



