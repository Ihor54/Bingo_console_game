import random
import sys
import time


class Bag:
    def __init__(self):
        self.barrels = [val for val in range(1, 91)]

    def choose(self):
        bar = random.choice(self.barrels)
        self.barrels.remove(bar)
        print('New barrel: ' + str(bar) + '(left ' + str(len(self.barrels)) + ')')
        print('New barrel: {} ')
        return bar


class Card:
    def __init__(self, name='Your card'):
        self.r = sorted(random.sample(range(1, 91), 15))
        self.name = name
        self.rows = []
        i = 0
        for _ in range(3):
            self.rows += self.dashes(self.r[i:i+5])
            i += 5
        self.num = len(self.rows)

    def mark(self, num):
        for i in range(0, len(self.rows)):
            if self.rows[i] == num:
                self.rows[i] = '-'
                self.num -= 1

    def set_name(self, name):
        self.name = name

    @staticmethod
    def dashes(row):
        it = iter(row)
        indeces = list(range(len(row) + 4))
        dash_indeces = set(random.sample(indeces, 4))
        row = ['__ ' if i in dash_indeces else next(it) for i in indeces]
        return row

    def __str__(self):
        s = ''
        ch_num = (26 - len(self.name)) / 2
        for _ in range(0, int(ch_num) + 1):
            s += '-'
        s += self.name
        for _ in range(0, int(ch_num)):
            s += '-'
        s += '\n'
        i = 0
        for _ in range(0, 3):
            s += ' ' + ' '.join(map(str, self.rows[i:i + 9]))
            s += '\n'
            i += 9
        s += '--------------------------'
        return s


class Player:
    def __init__(self, card):
        self.card = card


class User(Player):
    def __init__(self, card):
        Player.__init__(self, card)

    def check_b(self, barrel):
        z = input('Do you have such number? (y/n) \n')
        if z == 'y':
            if barrel in self.card.rows:
                self.card.mark(barrel)
                return 1
            else:
                return 0
        elif z == 'n':
            if barrel not in self.card.rows:
                return 1
            else:
                return 0
        else:
            return 0


class Computer(Player):
    def __init__(self, card):
        Player.__init__(self, card)
        self.card.set_name('Computer\'s card')

    def check_b(self, barrel):
        for val in self.card.rows:
            if barrel == val:
                self.card.mark(val)


modes = {
    '1': 'comp - user',
    '2': 'comp - comp',
    '3': 'user - user'
}


def pr_modes(md):
    for val in modes:
        print('{}. {}'.format(val, modes[val]))
    g_md = int(input('Choose the game mode '))
    return g_md


g_mode = pr_modes(modes)

card_1 = Card()
card_2 = Card()
bag = Bag()

while g_mode not in [1, 2, 3]:
    g_mode = pr_modes(modes)

if g_mode == 1:
    comp = Computer(card_1)
    user = User(card_2)
    print(card_1)
    print(card_2)
    while True:
        bg_val = bag.choose()
        print(card_1)
        print(card_2)
        comp.check_b(bg_val)
        if user.check_b(bg_val) == 0 or comp.card.num == 0:
            print('Computer won')
            sys.exit()
        if user.card.num == 0:
            print('You won')
            sys.exit()

elif g_mode == 2:
    comp_1 = Computer(card_1)
    comp_2 = Computer(card_2)
    print(card_1)
    print(card_2)
    while True:
        bg_val = bag.choose()
        comp_1.check_b(bg_val)
        comp_2.check_b(bg_val)
        print(card_1)
        print(card_2)
        time.sleep(2)
        if comp_1.card.num == 0:
            print('Computer 1 won')
            sys.exit()
        if comp_2.card.num == 0:
            print('Computer 2 won')
            sys.exit()
elif g_mode == 3:
    user_1 = User(card_1)
    user_2 = User(card_2)
    print(card_1)
    print(card_2)
    while True:
        bg_val = bag.choose()
        print(card_1)
        print(card_2)
        if user_1.check_b(bg_val) == 0 or user_2.card.num == 0:
            print('Player 2 won')
            sys.exit()
        if user_2.check_b(bg_val) == 0 or user_1.card.num == 0:
            print('Player 1 won')
            sys.exit()

if __name__ == '__main__':
    bag.choose()
]