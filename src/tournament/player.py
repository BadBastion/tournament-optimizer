import json


class Player:
    name = ""
    history = {}

    def __init__(self, name, history=None):
        self.name = name
        self.history = history or {}

    def __repr__(self):
        return self.name

    def play_table(self, table):
        opponent_names = [player.name for player in table if player.name != self.name]

        for name in opponent_names:
            self.history[name] = self.history.get(name, 0) + 1

    def __getitem__(self, name):
        return self.history.get(name, 0)

    def history_cost(self):
        cost = 0
        for play_count in self.history.values():
            cost += play_count ** 2

        return cost ** 0.5

    def flat_history_cost(self):
        cost = 0
        for play_count in self.history.values():
            cost += play_count

        return cost

    def min_history_cost(self, room_player_count):
        cost = 0
        for play_count in self.history.values():
            cost += play_count

        return (((cost / room_player_count) ** 2) * room_player_count) ** 0.5

