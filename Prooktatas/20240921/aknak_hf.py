#1. aknák elhelyezése egy rácsban
#2. számok kiszámítása az aknák körül
#3. a rács megjelítése színezéssel
#4. feltárás kezéelése
#5. Zászlók kezelése
#6. játék logika




import random


from  colorama import init, Fore, Style
from dotenv import load_dotenv
import os

load_dotenv()

init(autoreset=True)

GRID_SIZE = int(os.getenv('GRID_SIZE', 8))
NUM_MINES = int(os.getenv('NUM_MINES', 10))

#NUMBER_COLORS = {
#    '1': Fore.BLUE,
#    '2': Fore.GREEN,
#    '3': Fore.RED,
#    '4': Fore.MAGENTA,
#    '5': Fore.YELLOW,
#    '6': Fore.CYAN,
#    '7': Fore.LIGHTRED_EX,
#    '8': Fore.LIGHTBLUE_EX
#}

COLOR_MAPPING = {
    'BLUE': Fore.BLUE,
    'GREEN': Fore.GREEN,
    'RED': Fore.RED,
    'MAGENTA': Fore.MAGENTA,
    'YELLOW' : Fore.YELLOW,
    'CYAN': Fore.CYAN,
    'LIGHTRED': Fore.LIGHTRED_EX,
    'LIGHTBLUE': Fore.LIGHTBLUE_EX
}

NUMBER_COLORS = {
    str(i): COLOR_MAPPING.get(os.getenv(f'COLOUR_{i}')) for i in range(1, 9)
}

def create_minefield_1():
    grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    mines = set()

    while len(mines) < NUM_MINES:
        row = random.randint(0, GRID_SIZE -1)
        col = random.randint ( 0, GRID_SIZE -1)
        mines.add((row, col))

    for row, col in mines:
        grid[row][col] = 'M'

    return grid, mines


def create_minefiled(**kwargs):
    grid_size= kwargs.get('grid_size', GRID_SIZE)
    num_mines = kwargs.get('num_mines', NUM_MINES)

    grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    mines = set()

    while len(mines) < NUM_MINES:
        row = random.randint(0, GRID_SIZE -1)
        col = random.randint ( 0, GRID_SIZE -1)
        mines.add((row, col))

    for row, col in mines:
        grid[row][col] = 'M'

    return grid, mines


def calculate_numbers(grid):
    """
    Kell egy lista az összes iránnyal. A lista elemei egy poziciós tuple pár lesz (dr, dc)
    * dr => A sorban történő elmozuládok ˙(delta row)
    * dc => Az oszlopban történő elmoztulás ( delta calum)

    '''
    [(-1, -1), (-1, 0), (-1, 1),
    (0, -1),           ,(0, 1),
    (1, -1),  (1, 0),  (1, 1)]
    '''
    * (-1, -1): A mező bal felső szomszédja
    * (-1, 0): a mező felett levő szomszédja
    * (-1, 1): A mező jobb frlső szomszédja

    '''Rács (5x5)
    (1,1) (1,2) (1,3)
    (2,1) (2,2) (2,3)
    (3,1) (3,2) (3,3)
    '''
    Ha a bal felső szomszédot akarom megnézni(-1, -1)
    (row + dr, col + dc)
    (2 + -1, 2 + -1) = (1,1)

    """
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 'M':
                continue
            mine_count = 0
            for dr, dc in directions:
                r, c = row + dr, col +dc
                if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and grid[r][c] == 'M':
                    mine_count += 1
            grid[row][col] = str(mine_count) if mine_count > 0 else ' '


def colorize(text, *args):
    return ''.join(args) + text + Style.RESET_ALL

def display_grid(visible_grid, mines_left):
    print('\n   ' + ' '. join(str(i) for i in range(GRID_SIZE)))
    print(' ' + '---' * GRID_SIZE)
    for idx, row in enumerate(visible_grid):
        print(f'{idx} | ' + ' '.join(colorize(cell, NUMBER_COLORS.get(cell, Fore.YELLOW if cell == 'F' else Fore.RED if cell == 'M' else ''))
                                     for cell in row))

def reveal_cell_whit_recursion(grid, visible_grid, row, col):
    if visible_grid[row][col] != ' ':
        return False # Már egy feltárt mező

    if grid[row][col] == 'M':
        return True # Aknára léptünk

    # Ha üres mezőt találtunk feltárjuk:
    def flood_fill(r, c):
        """
        '''
        rács(grid):
        M 1 0 0
        1 2 0 0
        0 0 0 0
        0 0 0 0
        '''
        (2,2) => 0

        '''
        visible_grid:
        M 1
        1 2
        0 0
        0 0
        '''
        """
        # Rács határain belül vagyunk (rekurzió kilép a rácsból)
        if not (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
            return
        # Ha a mező már feltárt vagy akna a fgv nem folytatja a rekurziót
        if visible_grid[r][c] != ' ' or grid[r][c] == 'M':
            return
        # Mező feltárása
        # ha a mező nem tartalmaz számot, feltárja azt, és láthatóvá teszi
        visible_grid[r][c] = grid[r][c]
        if grid[r][c] == ' ':
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]:
                flood_fill(r + dr, c + dc)
    flood_fill(row,  col)
    return False

def reveal_cell(grid, visible_gird, row, col):
    if visible_gird[row][col] != ' ':
        return False

    if grid[row][col] == 'M':
        return True

# iteraktív feltárás az üres mezők esetén
    stack = [(row, col)]
    processed = set()
    while stack:
        r, c = stack.pop()
        if not (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
            continue

        if (r, c) in processed:
            continue

        if visible_gird[r][c] != ' ' or grid[r][c] == 'M':
            continue

        processed.add((r, c))
        visible_gird[r][c] = grid[r][c]

        if grid[r][c] == ' ':
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
                            (0, -1),           (0, 1),
                            (1, -1),  (1, 0),  (1, 1)]:
                nr, nc = r+ dr, c + dc
                if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                    if grid[nr][nc] == ' ' and (nr, nc) not in processed:
                        stack.append((nr, nc))
                    elif grid[nr][nc] != 'M' and (nr, nc) not in processed:
                        visible_gird[nr][nc] = grid[nr][nc]
    return False



def toggle_flag(visible_grid, row, col):
    if visible_grid[row][col] == ' ':
        visible_grid[row][col] = 'F'
    elif visible_grid[row][col] == 'F':
        visible_grid[row][col] = ' '

def play():
    grid, mines = create_minefiled()  # Létrehozza a mezőt és az aknákat
    calculate_numbers(grid)  # Kiszámítja a számokat
    visible_grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Kezdeti látható mező (üres)

    revealed_cells = 0  # Feltárt mezők száma
    total_cells = GRID_SIZE * GRID_SIZE - NUM_MINES  # Összes feltárható mező
    flags_left = NUM_MINES  # Hátralévő zászlók száma

    # Játék fő ciklusa
    while revealed_cells < total_cells:
        display_grid(visible_grid, flags_left)  # Megjeleníti a grid-et
        print("\nUtmutató:")
        print("- 'R <sor> <oszlop>' :Mező feltárása (pl.: 'R 3 4' => feltárja a 3. sor 4. oszlopát)")
        print("- 'F <sor> <oszlop>' : Zászló elhelyezése (pl.: 'F 3 4' => zászlót helyez a 3. sor 4. oszlopára)")
        print("- A koordináták tartománya: 0-tól", GRID_SIZE - 1, "-ig terjedhet")
        print("- A zászlókat az aknák gyanús helyeire teheted")
        print("- Ha aknára lépsz, a játék véget ér")

        command = input("Adja meg egy parancsot (pl.: R 3 4): ").strip().upper()
        parts = command.split()

        if len(parts) != 3 or parts[0] not in ['F', 'R']:
            print('Érvénytelen parancs! Használj "R" vagy "F" parancsot a megfelelő formátumban.')
            continue

        try:
            action, row, col = parts[0], int(parts[1]), int(parts[2])
        except ValueError:
            print('Érvénytelen input, Használj számokat a koordináták megadásánal')
            continue

        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            print("Érvémytelen koordinátát adott meg! A sorok és oszlopok tartománya 0-tól", GRID_SIZE -1, "ig")
            continue

        if action == "F":
            toggle_flag(visible_grid, row, col)
            flags_left = NUM_MINES - sum(row.count('F') for row in visible_grid)
        elif action == 'R':
            hit_mine = reveal_cell(grid, visible_grid, row, col)
            if hit_mine:
                print('\nBUMMM!!!! Aknát találtál!')
                for r, c in mines:
                    visible_grid[r][c] = "M"
                display_grid(visible_grid, flags_left)
                print('Vége a játéknak!')
                return
            #Frissítjük a feltárt mezők számát
            revealed_cells = sum(1 for row in range(GRID_SIZE) for col in range(GRID_SIZE) if visible_grid[row][col] not in [' ', 'F'])
    print('\nGratulálok minden biztonságos mezőt feltártál!')
    display_grid(visible_grid, flags_left)

if __name__ == '__main__':
    play()
