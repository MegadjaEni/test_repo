from random import shuffle

class CardData:
    """Static class for the card data"""

    def __init__(self):
        # noinspection SpellCheckingInspection
        raise RuntimeError('Az osztály statikus, nem példányosítható')

    # noinspection SpellCheckingInspection
    colors = ('Kör', 'Káró', 'Treff', 'Pikk')
    # noinspection SpellCheckingInspection (nem húzza alá a szavakat)
    ranks = ('Kettő', 'Három', 'Négy', 'Öt', 'Hat', 'Hét', 'Nyolc', 'Kilenc', 'Tíz', 'Bubi', 'Dáma', 'Király', 'Ász')

    @staticmethod
    def get_value(what):
        values = {'Kettő': 2, 'Három': 3, 'Négy': 4, 'Öt': 5, 'Hat': 6,
                  'Hét': 7, 'Nyolc': 8, 'Kilenc': 9, 'Tíz': 10,
                  'Bubi': 10, 'Dáma': 10, 'Király':10, 'Ász': 11}
        if not what in values.keys():
            raise ValueError('A megadott érték nem található')
        return values[what]


    is_playing = True

class Card:

    def __init__(self, color, rank):
        self.color = color
        self.rank = rank

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if len(color) >= 3:
            self.__color = color
        else:
            raise ValueError('Az érték nem egy kártyaszín')

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def renk(self, rank):
        if len(rank) >= 2:
            self.__rank = rank
        else:
            raise ValueError('Az érték minimun 2 karakteres legyen')

    def __str__(self):
        return self.rank + ' - ' + self.color


class Deck(list):
    def __init__(self):
        super().__init__()
        #self.cards_deck = []
        for color in CardData.colors:
            for rank in CardData.ranks:
                self.append(Card(color, rank))

    def __str__(self):
        tmp = ''
        for card in self:
            tmp += card.__str__() + "\n"
        return tmp

    def mix(self):
        shuffle(self)

    def div(self):
        return self.pop()

    def append(self, card):
        if not isinstance(card, Card):
            raise TypeError('Csak kártya tipusút lehet hozzáadni')
        super().append(card)


class Hand(list):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.ace = 0

    def append(self, card):
        if not isinstance(card, Card):
            raise TypeError('Csak kártya tipusú objektumot lehet hozzáadni')
        super().append(card)
        self.value += CardData.get_value(card.rank)
        if card.rank == 'Ász':
            self.ace += 1

    def set_aces(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1


class Tokens:

    def __init__(self, summa=100):
        self.sum = summa
        self.bet = 0

    @property
    def sum(self):
        return self.__sum

    @sum.setter
    def sum(self, value):
        if value > 0:
            self.__sum = value
        else:
            raise ValueError('Az érték nem lehet negatív vagy 0')

    @property
    def bet(self):
        return self.__sum

    @bet.setter
    def bet(self, value):
        if value >= 0 and self.sum - value >= 0:
            self.__bet = value
        else:
            raise ValueError('A tét csak pozítiv egész szám lehet,'
                             "és nem adhat több tétet mint amennyi zsetonja van.")

    def win_bet(self):
        self.__sum += self.bet

    def loose_bet(self):
        self.__sum -= self.bet

class Rules:
    def __init__(self):
        raise NotImplementedError()

    @staticmethod
    def betting(chips: Tokens):
        while True:
            try:
                chips.bet = int(input("Mennyi  zsetont szeretne feltenni? "))
            except ValueError:
                print('Sajnálom az érték nem megfelelő!')
            else:
                break


    @staticmethod
    def draw(cards_deck, hand: Hand):
        hand.append(cards_deck.div())
        hand.set_aces()

    @staticmethod
    def draw_or_stop(cards_deck: Deck, hand: Hand):
        while True:
            var = input('Huzni szeretne vagy megállni? "h"-t vagy "m"-t:')
            if var[0].lower() == 'h':
                Rules.draw(cards_deck, hand)
            elif var[0].lower() == 'm':
                print('A játékos megállt! Az osztó játszik')
                CardData.is_playing = False
            else:
                print('Ilyen opció nincs')
                continue
            break

    @staticmethod
    def player_cards(card_player: Hand):
        print('A játékos kezében van:\n', *card_player, sep='\n')
        print('A játékos kezében lévő lapok összeértéke: ', card_player.value)


    @staticmethod
    def not_show_all(card_player: Hand, card_dealer: Hand):
        print('Aaz osztó kezében van: ')
        print('<kártyalap rejtve>')
        print(card_dealer[1])
        Rules.player_cards(card_player)

    @staticmethod
    def show_all(card_player: Hand, card_dealer: Hand):
        print('Az osztó kezében van:\n', *card_dealer, sep='\n')
        print('A játékos kezében lévő lapok összértéke:\n', card_player.value)
        Rules.player_cards(card_player)

    @staticmethod
    def player_loose(chips: Tokens):
        print('A játékos elúszott')
        chips.loose_bet()

    @staticmethod
    def player_win(chips: Tokens):
        print('A játékos nyert!')
        chips.win_bet()

    @staticmethod
    def dealer_loose(chips: Tokens):
        print('A osztó elúszott!')
        chips.loose_bet()

    @staticmethod
    def dealer_win(chips: Tokens):
        print('A osztó nyert!')
        chips.win_bet()

    @staticmethod
    def equal(chips: Tokens):
        print('Az állás döntetlen, az osztó nyert!')
        chips.loose_bet()


token = Tokens()

while True:
    print('Üdvözlöm kedves játékos a BlackJack játékban! A cél elérni a 21-et\n'
          'Az osztó addig húz, amíg el nem érni a 17-et\n'
          'Az Ász a szabályok szerint 11-et vagy 1-et ér')
    deck = Deck()
    deck.mix()

    player = Hand()
    dealer = Hand()

    Rules.draw(deck, player)
    Rules.draw(deck, player)
    Rules.draw(deck, dealer)
    Rules.draw(deck, dealer)

    Rules.betting(token)
    Rules.not_show_all(player, dealer)
    while CardData.is_playing:
        Rules.draw_or_stop(deck, player)
        Rules.not_show_all(player, dealer)
        if player.value > 21:
            Rules.player_loose(token)
        if player.value <= 21:
            while dealer.value < 17:
                Rules.draw(deck, dealer)
                if dealer.value > 21:
                    Rules.dealer_loose(token)
                elif dealer.value > player.value:
                    Rules.dealer_win(token)
                elif dealer.value < player.value:
                    Rules.player_win(token)
                else:
                    Rules.equal(token)
    print('\nA játékos egyeblege: ', token.sum)
    new_game = input('Szeretne még 1X játszani? i-igen vagy n-nem: ')
    if new_game[0].lower() == 'i':
        CardData.is_player = True
        continue
    print('Köszönjük a játékot!')
    break




    