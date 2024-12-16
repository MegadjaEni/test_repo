# 1. kategorizált szólisták különböző nehézségi szintekkel
# 2. nehézségi szint kiválasztása
# 3. véletlenszerű szó kiválasztása
# 4. valamilyen akasztófa
# 5. statisztika megjelenítése az aktuális állapotról
# 6.felhasználói imput kezelése
# 7. kiírt rejtett szó frissítése
# 8. győzelem, vereség stb...
import random


def get_word_list(difficulty: str):
    """
    kategorizalt szolistak kulombozo nehezsegi szintekkel
    :param difficulty: Nehezsegi szint
    :return: A kategorizalt szavak
    """
    easy_words = ['cat', 'dog', 'hat', 'sun', 'tree']
    medium_words = ['python', 'guitar', 'teacher', 'jungle', 'planet']
    hard_words = ['complicated', 'encyclopedia', 'worcestershire', 'onomatopoeia', 'anachronism']

    if difficulty == 'easy':
        return easy_words
    elif difficulty == 'medium':
        return medium_words
    return hard_words


def choose_difficulty() -> str:
    """
    nehezsegi szint kivalasztasa
    :return: Nehezsegi szint
    """
    while True:
        diff = input('Válassz egy nehézésgi szintet(easy, medium, hard): ').lower()
        if diff in ['easy', 'medium', 'hard']:
            return diff
        print('Érvénytelen választás! Csak easy, medium vagy hard lehet!')


def choose_word(word_list: list[str]) -> str:
    """
    véletlenszerű szó kiválasztása
    :param word_list: szavakat tartalmazo lista
    :return: Kiválasztott szó
    """
    return random.choice(word_list).upper()


def draw_hangman(tries_left: int):
    """
    akasztófa
    :param tries_left: próbálkozások száma
    :return:
    """
    stages = [
        """
        --------
        |      |
        |
        |
        |
        ---
        """,
        """
        --------
        |      |
        |      O
        |
        |
        ---
        """,
        """
        --------
        |      |
        |      O
        |      |
        |
        ---
        """,
        """
        --------
        |      |
        |      O
        |     /|
        |
        ---
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |
        ---
        """,
        """
         --------
        |      |
        |      O
        |     /|\\
        |     /
        ---
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |     /\\
        ---
        """
    ]
    print(stages[6 - tries_left])

def desplay_game_state(hidden_word, incorrect_guesses: list[str], tries_left: int):
    """
    Statisztika megjelítése az aktuális álláspontról
    :param hidden_word: A rejtett szó
    :param incorrect_guesses: Rossz betűk száma
    :param tries_left: Jó próbálkozások száma
    :return:
    """
    draw_hangman(tries_left)
    print("\nJelenlegi állás:")
    print(" ".join(hidden_word))
    print("Hibás próbálkozások száma",len(incorrect_guesses))
    print('Hibás próbálkozások: '," ".join(incorrect_guesses))
    print("Hátralevő probálkozások száma: ", tries_left)

def get_player_guess(incorrect_guesses: list[str], correct_guesses: list[str]) -> str:
    """
    felhasználói input kezelése
    :param incorrect_guesses: hibás próbálkozások
    :param correct_guesses: helyes próbálkozások
    :return: Tipp
    """
    while True:
        guess = input('Kérlek adj meg egy betűt: ').upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Csak egyetlen betűt adj meg!")
        elif guess in incorrect_guesses or guess in correct_guesses:
            print("Ezt a betűt már próbáltad")
        else:
            return guess

def update_hidden_word(word: list[str], hidden_word: str, guess: str):
    """
    Rejtett szó módosítása
    :param word: A feladvány szava
    :param hidden_word: Rejtett szó
    :param guess: tipp
    :return:
    """
    for i, char in enumerate(word):
        if char == guess:
            hidden_word[i] = guess



def is_game_lost(tries_left: int):
    """
    Vesztett e a játékos
    :param tries_left: probálkozások száma
    :return: Vesztett e
    """
    return tries_left <= 0


def is_game_won(hidden_word: list[str]):
    """
    Nyert e a játékos
    :param hidden_word: Rejtett szó
    :return: Nyert e
    """
    return '_' not in hidden_word


def display_statistics(stats: dict[str]):
    """
    statiszika megjelenítése
    :param stats: Statisztikai adatok
    :return:
    """
    print("\nJáték statisztikák:")
    print(f"Összes játék: {stats['total_games']}")
    print(f"Győzelmek: {stats['games_won']}")
    print(f"Helyesen kitalált szavak: {', '.join(stats['words_guessed'])}")
    print(f"Hátralevő próbálkozzások a győztes játékokban: {stats['tries_renaining']}")

def update_statistics(stats: dict, won: bool, word: str, tries_left: int):
    """
    :param stats: statisztikai adatokat tartalmazó szótár
    :param won: Nyert e a játékos
    :param word: A feladvány szava
    :param tries_left: próbálkozások száma
    :return:
    """
    stats['total_games'] += 1
    if won:
        stats['games_won']+= 1
        stats['words_guessed'].append(word)
        stats['tries_remaining'].append(tries_left)


def display_game_state(hidden_word, incorrect_gesses, tries_left):
    pass


def updata_hidden_word(word, hidden_word, guess):
    pass


def main():
    stats = {'total_games': 0, 'games_won': 0, 'words_guessed': [], 'tries_remaining': 0}
    print('Üdvözöljük az akasztófa játékban!')
    while True:
        difficulty = choose_difficulty()
        word_list = get_word_list(difficulty)
        word = choose_word(word_list)
        hidden_word = ['_'] * len(word)
        incorrect_gesses = []
        correct_guesses = []
        tries_left = 6
        game_over = False

        while not game_over:
            display_game_state(hidden_word, incorrect_gesses, tries_left)
            guess = get_player_guess(incorrect_gesses, correct_guesses)

            if guess in word:
                correct_guesses.append(guess)
                updata_hidden_word(word, hidden_word, guess)
                if is_game_won(hidden_word):
                    print(f"\nGratulálunk! Megnyerted a játékot! A helyes szó: {word} ")
                    game_over = True
                    update_statistics(stats, True, word, tries_left)
            else:
                incorrect_gesses.append(guess)
                tries_left -= 1
                if is_game_lost(tries_left):
                    draw_hangman(0)
                    print(f"\nSajnálom vesztettél! A helyes szó: {word}")
                    game_over = True
                    update_statistics(stats, False,word, tries_left)
        display_statistics(stats)

        if not input('Szeretnél újra játszani? (Igen/Nem): ').lower().startswith('i'):
            print("viszlát! Köszönöm a játékot!")
            break
main()
