from itertools import combinations


class Table:
    seats = []
    size = 0

    def __init__(self, size=0, players=None):
        if players is not None:
            self.size = len(players)
            self.seats = list(players)
        else:
            if size < 0:
                raise Exception('Cant create a Table of size less than 0')
            self.seats = [None] * size
            self.size = size

    def __repr__(self):
        return f'[{ ", ".join([repr(s) for s in self.seats]) }]'

    def __setitem__(self, number, player):
        if -1 < number < self.size:
            self.seats[number] = player

    def __getitem__(self, number):
        if -1 < number < self.size:
            return self.seats[number]

    def __iter__(self):
        return iter(self.seats)

    def cost(self):
        cost = 0
        for player, opponent in combinations(self.seats, 2):
            cost += player[opponent.name] ** 2

        return cost ** 0.5
