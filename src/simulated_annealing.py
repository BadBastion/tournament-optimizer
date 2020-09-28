import random
from math import floor
from src.tournament.room import random_room


def random_swap(player_count, table_size):
    left_player = random.randrange(player_count)
    # Since we don't want to swap two people at the same table
    # we subtract one table from the range.
    right_player = random.randrange(player_count - table_size)

    left_table = floor(left_player / table_size)
    right_table = floor(right_player / table_size)

    # Shift the results so the right_player never collides with left_player
    if right_table >= left_table:
        right_player += table_size
        right_table += 1

    left_swap = (left_table, left_player % table_size)
    right_swap = (right_table, right_player % table_size)

    return left_swap, right_swap



def calculate_heat(iteration, max_iterations):
    normal_progress = iteration + 1 / max_iterations
    # logarithmically degrees speed from 1 to 0 as we make progress
    return normal_progress ** 2



def move_rating(old_cost, new_cost, heat):
    cost_delta = (old_cost - (new_cost+0.01)) / (new_cost+0.01)
    normal_cost_delta = 1 + cost_delta

    # Returning early saves us from multiplying too many times
    if normal_cost_delta > 1:
        return 1
    else:
        return normal_cost_delta ** (1 + heat * 5)


def simulated_annealing(players, table_size, iterations=1000):
    player_count = len(players)
    room = random_room(players, table_size)
    cost = room.cost()

    for i in range(iterations):
        swap = random_swap(player_count, table_size)
        new_cost = room.cost_after_swap(swap)
        heat = calculate_heat(i, iterations)

        if move_rating(cost, new_cost, heat) > random.random():
            room.swap(swap)
            cost = new_cost

    return room, cost



