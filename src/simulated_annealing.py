import random
from math import floor


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
    normal_progress = 1 - (iteration / max_iterations)
    # reduces heat from 1 to 0 as we make progress
    return normal_progress ** 2


ONE_MILLIONTH = 10 ** -6
def move_rating(old_cost, new_cost, heat):
    cool = 1 - heat  # not being hot is pretty cool
    new_cost = max(ONE_MILLIONTH, new_cost)  # diving by zero is bad for our health.
    cost_delta = (old_cost - new_cost) / new_cost

    if cost_delta < 0:
        # When the move makes cost worse we see a negative delta from 0 to -1
        # In this case heat
        normal_cost_delta = 1 + cost_delta
        heat_exponent = 3 + cool * 5
    else:
        normal_cost_delta = 1 / (1 + cost_delta)
        heat_exponent = 1 / (1 + cool * 5)

    return normal_cost_delta ** heat_exponent


def simulated_annealing(starting_room, players, table_size, iterations=1000):
    player_count = len(players)
    room = starting_room
    cost = starting_room.cost()

    for i in range(iterations):
        swap = random_swap(player_count, table_size)
        new_cost = room.cost_after_swap(swap)
        heat = calculate_heat(i, iterations)

        if move_rating(cost, new_cost, heat) > random.random():
            room.swap(swap)
            cost = new_cost

    return room



