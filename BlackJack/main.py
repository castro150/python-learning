import random


class Card(object):
    def __init__(self, label, value, quantity=4):
        self.label = label
        self.value = value
        self.quantity = quantity

    def can_remove(self):
        return self.quantity > 0

    def remove(self):
        if self.can_remove():
            self.quantity -= 1


class Deck(object):
    def __init__(self):
        self.cards = []
        self.quantity = 0

    def initialize(self):
        self.cards.append('')
        self.cards.append(Card('1 or 11', 1, 4))

        for index in range(2, 14):
            value = 10 if index > 10 else index
            self.cards.append(Card(str(index), value, 4))

        self.quantity = 4 * 13

    def buy_card(self):
        if self.quantity == 0:
            return ''

        card_index = random.randint(1, 13)
        while not self.cards[card_index].can_remove():
            card_index = random.randint(1, 13)

        self.quantity -= 1
        self.cards[card_index].remove()
        return self.cards[card_index]


class Player(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []

    def receive_card(self, card):
        self.cards.append(card)

    def can_bet(self, value):
        return self.money - value >= 0

    def bet(self, value):
        if self.can_bet(value):
            self.money -= value

    def print_money(self):
        print 'You have ' + str(self.money)

    def print_cards(self):
        print '\n' + self.name + ':'
        for card in self.cards:
            print card.label
        print 'Points: ' + str(self.sum_points())

    def sum_points(self):
        points = 0
        ases = 0
        for card in self.cards:
            if card.value != 1:
                points += card.value
            else:
                ases += 1

        points += ases
        for a in range(ases):
            if points + 10 <= 21:
                points += 10
            else:
                break

        return points


def play(deck, player, dealer):

    player.print_money()
    bet = int(raw_input('What is your bet?'))
    while not player.can_bet(bet):
        player.print_money()
        bet = int(raw_input('Invalid value! Try another one?'))
    player.bet(bet)

    dealer.receive_card(deck.buy_card())
    dealer.print_cards()

    player.receive_card(deck.buy_card())
    player.print_cards()
    buy_another = raw_input('Want to buy another card?').lower().startswith('y')
    while buy_another:
        player.receive_card(deck.buy_card())
        player.print_cards()
        buy_another = raw_input('Want to buy another card? (y/n)').lower().startswith('y')

    while dealer.sum_points() <= 17:
        dealer.receive_card(deck.buy_card())

    dealer.print_cards()

    if player.sum_points() <= 21:
        if player.sum_points() > dealer.sum_points() or dealer.sum_points() > 21:
            player.money += 2 * bet
            print 'You won!'
        elif player.sum_points() < dealer.sum_points():
            print 'You lose.'
        else:
            player.money += bet
            print 'Draw.'
    else:
        print 'You lose.'

    if raw_input('Want to play again? (y/n)').lower().startswith('y'):
        deck.initialize()
        player.cards = []
        dealer.cards = []
        play(deck, player, dealer)


def start():
    deck = Deck()
    deck.initialize()

    name = raw_input('What is your name?')
    money = int(raw_input('What is your money?'))

    player = Player(name, money)
    dealer = Player('Dealer', 0)

    play(deck, player, dealer)


start()
