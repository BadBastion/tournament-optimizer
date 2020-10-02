from src.simulated_annealing import simulated_annealing
from src.tournament.room import random_room
import math


def simulated_annealing_ensemble(players, table_size, iterations=500, actors=500):

    best_room = None
    best_room_cost = math.inf

    for i in range(actors):
        starting_room = random_room(players, table_size)

        optimized_room = simulated_annealing(starting_room, players, table_size, iterations)

        if optimized_room.cost() < best_room_cost:
            best_room = optimized_room
            best_room_cost = optimized_room.cost()

    return best_room, best_room_cost


