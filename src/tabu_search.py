from random import shuffle
import math
from src.tournament import Room, Table, Player


def random_room(players, table_size):
    shuffle(players)

    table_count = math.floor(len(players) / table_size)
    remainder = len(players) % table_size

    tables = []

    for table_i in range(table_count):
        table = Table(table_size)
        for player_i in table_size:
            table[player_i] = players[table_i * 4 + player_i]
        tables.append(table)

    # Handle players that don't fit into a table
    remainder_table = Table(remainder)
    for player_i in range(remainder):
        remainder_table[player_i] = players[table_count * 4 + player_i]
    tables.append(remainder_table)

    return Room(tables)


def tabu_search(players, table_size):
    solution = random_room(players, table_size)
    return solution
