import os
from platform import system
import random

PLAYER1_NAME = 'Játékos 1'
PLAYER2_NAME = 'Játékos 2'

def clear_screen():
    if system().lower().startswith('win'):
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

def show_table(table):
    clear_screen()
    print('   |   |')
    print(' ' + table[7] + ' | ' + table[8] + ' | ' + table[9])
    print('   |   |')
    print('-' * 11)
    print('   |   |')
    print(' ' + table[4] + ' | ' + table[5] + ' | ' + table[6])
    print('   |   |')
    print('-' * 11)
    print('   |   |')
    print(' ' + table[1] + ' | ' + table[2] + ' | ' + table[3])
    print('   |   |')

#test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'O', 'X']
#show_table(test_board)
def input_player():
    marker = ''

    while not ( marker == 'X' or marker == 'O'):
        marker = input(PLAYER1_NAME + ': Mivel szeretnél lenni az X vagy az O-val? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return ('O', 'X')
#input_player() ez csak teszt volt


def set_marker(table, marker, pos):
    table[pos] = marker

#set_marker(test_board, '*', 5)
#show_table(test_board)


def check_winning(table, marker):
    return (
        (table[7] == marker and table[8] == marker and table[9] == marker) or # felső sor
        (table[4] == marker and table[5] == marker and table[6] == marker) or  # középső sor
        (table[1] == marker and table[2] == marker and table[3] == marker) or # alsó sor
        (table[7] == marker and table[4] == marker and table[1] == marker) or  # bal oszlop
        (table[8] == marker and table[5] == marker and table[2] == marker) or  # középső oszlop
        (table[9] == marker and table[6] == marker and table[3] == marker) or  # jobb oszlop
        (table[7] == marker and table[5] == marker and table[3] == marker) or  # bal átló
        (table[9] == marker and table[5] == marker and table[1] == marker)  # jobb átló
    )

#print(check_winning(test_board, 'O'))

def random_player():
    if random.randint(0, 1) == 0:
        return PLAYER1_NAME
    return PLAYER2_NAME

def check_whitespace(table, pos):
    return table[pos] == ' '

def is_table_full(table):
    for i in range(1, 10):
        if check_whitespace(table, i):
            return False
        return True

def choose_player_position(table):
    pos = 0

    while pos not in range(1, 10) or not check_whitespace(table, pos):
        user_input = input('Kérem adjon meg egy pozíciót (1-9): ')
        if user_input.isdigit():
            pos = int(user_input)
            clear_screen()

    return pos

def repeat_game():
    return input('Szeretne újra játszani? Írja be, hogy Igen vagy Nem: ').lower().startswith('i')


def run_player_logic(marker, name):
    global game_on
    global who
    show_table(table)
    position = choose_player_position(table)
    set_marker(table, marker, position)

    if check_winning(table, marker):
        show_table(table)
        print('Gratulálok! Megnyerted a játékot')
        game_on = False
    else:
        if is_table_full(table):
            show_table(table)
            print('A játék döntetlen!')
            game_on = False
        else:
            who = name

print('Üdvözöljük az IX_OX játékban!')

while True:
    table = [' '] * 10
    player1_marker, player2_marker = input_player()
    who = random_player()
    print(who + ' jön először')

    start_game = input('Készen vagy a játékra? Írd be, hogy Igen vagy Nem: ')

    if start_game.lower().startswith('i'):
        game_on = True
    else:
        game_on = False

    while game_on:
        if who == PLAYER1_NAME:
            run_player_logic(player1_marker, PLAYER2_NAME)
            show_table(table)
            position = choose_player_position(table)
            set_marker(table, player1_marker, position)

            if check_winning(table, player1_marker):
                show_table(table)
                print('Gratulálok! Megnyerted a játékot')
                game_on = False
            else:
                if is_table_full(table):
                    show_table(table)
                    print('A játék döntetlen!')
                    game_on = False
                    break
                else:
                    who = PLAYER2_NAME
        else:
            run_player_logic(player2_marker, PLAYER1_NAME)
            show_table(table)
            position = choose_player_position(table)
            set_marker(table, player2_marker, position)

            if check_winning(table, player2_marker):
                show_table(table)
                print('Gratulálok! Megnyerted a játékot')
                game_on = False
            else:
                if is_table_full(table):
                    show_table(table)
                    print('A játék döntetlen!')
                    game_on = False
                    break
                else:
                    who = PLAYER1_NAME
    if not repeat_game():
        break