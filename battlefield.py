from fleet import Fleet
from herd import Herd

# Gameplay: Welcome screen. Choose side. If robots, choose weapons. If dinosaurs, choose dinos? Begin battle. You pick your attacks, opponent attacks random?


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass

    def display_welcom(self):
        pass

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass