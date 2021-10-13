from fleet import Fleet
from herd import Herd

# Gameplay: Welcome screen. Choose side. If robots, choose weapons. If dinosaurs, choose dinos? Begin battle. You pick your attacks, opponent attacks random?


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle(self):
        pass

    def dino_turn(self):
        opponent = self.show_robo_opponent_options()
        dinosaur = input(f"Which dinosaur should attack?  1 - {self.herd.dinosaurs[0]} 2 - {self.herd.dinosaurs[1]} 3 - {self.herd.dinosaurs[2]}  ")
        if dinosaur == "1":
            self.herd.dinosaurs[0].attack(opponent)
        elif dinosaur == "2":
            self.herd.dinosaurs[1].attack(opponent)
        if dinosaur == "3":
            self.herd.dinosaurs[2].attack(opponent)

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        opponent = input(f"Which robot do you want to attack? 1 - {self.fleet.robots[0]} 2 - {self.fleet.robots[1]} 3 - {self.fleet.robots[2]}")
        if opponent == "1":
            return self.fleet.robots[0]
        elif opponent == "2":
            return self.fleet.robots[1]
        elif opponent == "3":
            return self.fleet.robots[2]

    def display_winners(self):
        pass