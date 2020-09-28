import math
import random
from itertools import combinations, product
from src.tournament.table import Table


class Room:
    tables = []

    def __init__(self, tables):
        self.tables = tables

    def __repr__(self):
        return f'[{", ".join([repr(t) for t in self.tables])}]'

    def swap(self, swap):
        left, right = swap
        (left_table, left_chair) = left
        (right_table, right_chair) = right

        left_player = self.tables[left_table][left_chair]
        right_player = self.tables[right_table][right_chair]

        self.tables[left_table][left_chair] = right_player
        self.tables[right_table][right_chair] = left_player

    def cost_after_swap(self, swap):
        self.swap(swap)
        cost = self.cost()
        self.swap(swap)

        return cost

    def cost(self):
        cost = 0
        for table in self.tables:
            cost += table.cost()

        return cost

    # def adjacent(self):
    #     options = []
    #
    #     table_options = range(len(self.tables))
    #     for (left_table_i, right_table_i) in combinations(table_options, 2):
    #
    #         left_table = self.tables[left_table_i]
    #         right_table = self.tables[right_table_i]
    #
    #         left_table_options = range(len(left_table))
    #         right_table_options = range(len(right_table))
    #
    #         for (left_player_i, right_player_i) in product(left_table_options, right_table_options):
    #             left = (left_table, left_player_i)
    #             right = (right_table_i, right_player_i)
    #
    #             self.swap(left, right)
    #             cost = self.cost()
    #             self.swap(left, right)  # undo swap for now
    #
    #             options.append((left, right, cost))
    #
    #     return options


def random_room(players, table_size):
    random.shuffle(players)

    table_count = math.floor(len(players) / table_size)
    remainder = len(players) % table_size

    tables = []

    for table_i in range(table_count):
        table = Table(table_size)
        for player_i in range(table_size):
            table[player_i] = players[table_i * 4 + player_i]
        tables.append(table)

    # Handle players that don't fit into a table
    remainder_table = Table(remainder)
    for player_i in range(remainder):
        remainder_table[player_i] = players[table_count * 4 + player_i]
    tables.append(remainder_table)

    return Room(tables)