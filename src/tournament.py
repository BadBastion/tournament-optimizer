from itertools import combinations, product
import json


class Player:
    name = ""
    history = {}

    def __init__(self, name, history=None):
        self.name = name
        self.history = history or {}

    def __repr__(self):
        return f'{{ "name": "{self.name}", "history: {json.dumps(self.history)} }}'

    def play_table(self, table):
        opponent_names = [player.name for player in table if player.name != self.name]

        for name in opponent_names:
            self.history[name] = self.history.get(name, 0) + 1

    def cost(self):
        cost = 0
        for play_count in self.history.values():
            cost += play_count ** 2

        return cost ** 0.5

    def flat_cost(self):
        cost = 0
        for play_count in self.history.values():
            cost += play_count

        return cost


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
        for player in self.seats:
            cost += player.cost()

        return cost


class Room:
    tables = []

    def __init__(self, tables):
        self.tables = tables

    def __repr__(self):
        return f'[{ ", ".join([repr(t) for t in self.tables]) }]'

    def swap(self, left, right):
        (left_table, left_chair) = left
        (right_table, right_chair) = right

        left_player = self.tables[left_table][left_chair]
        right_player = self.tables[right_table][right_chair]

        self.tables[left_table][left_chair] = right_player
        self.tables[right_table][right_chair] = left_player

    def cost(self):
        cost = 0
        for table in self.tables:
            cost += table.cost()

        return cost

    def adjacent(self):
        options = []

        table_options = range(len(self.tables))
        for (left_table_i, right_table_i) in combinations(table_options, 2):

            left_table = self.tables[left_table_i]
            right_table = self.tables[right_table_i]

            left_table_options = range(len(left_table))
            right_table_options = range(len(right_table))

            for (left_player_i, right_player_i) in product(left_table_options, right_table_options):
                left = (left_table, left_player_i)
                right = (right_table_i, right_player_i)

                self.swap(left, right)
                cost = self.cost()
                self.swap(left, right)  # undo swap for now

                options.append((left, right, cost))

        return options
