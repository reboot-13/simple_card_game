import games

class Card:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['черви', 'пики', 'крести', 'буби']
    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.point = Card.RANKS.index(self.rank) + 2
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = self.rank + ' - ' + self.suit
        else:
            rep = 'xx'
        return rep

class Hand:
    def __init__(self):
        self.cards = []
        self.points = 0
    def __str__(self):
        rep = ''
        for i in range (2):
            rep = rep + str (self.cards[i]) + '\t'
            if len(self.cards) < 2:
                break
        return rep


    def add (self, card):
        self.cards.insert(0, card)

    def compare_cards (self):
        card_is_higher = False
        card_is_lower = False
        ask_decision = games.yes_or_no ('Следующая карта будет больше предыдущей? (y/n): ')
        if self.cards[0].point >= self.cards[1].point:
            card_is_higher = True
        else:
            card_is_lower = True
        if ask_decision == 'y' and card_is_higher:
            self.points += 1
            print('Угадал! \nКоличество очков: ',  self.points, '\n')
        elif ask_decision == 'n' and card_is_lower:
            self.points += 1
            print('Угадал! \nКоличество очков: ', self.points, '\n')


class Deck:
    def __init__(self):
        self.deck = []
        self.create()
        self.shuffle()

    def __str__(self):
        rep = ''
        for card in self.deck:
            rep = rep + str (card) + '\t'
        return rep

    def create (self):
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.deck.append(Card (rank, suit))

    def shuffle (self):
        import random
        random.shuffle(self.deck)

    def give_card (self, other_hand):
        top_card = self.deck[0]
        self.deck.remove(top_card)
        other_hand.add (top_card)

def main ():
    print('Добро пожаловать в карточную игру! \nПравила игры: в начале диллер выдаёт вам одну карту, '
          'ваша задача: угадать,\nбудет ли следующая карта в колоде больше или меньше последней полученной вами карты.\n'
          'Удачи!')
    game_deck = Deck ()
    player = Hand ()
    game_deck.give_card(player)
    print(player)
    while game_deck.deck:
        game_deck.give_card(player)
        player.compare_cards()
        print(player)
main ()

