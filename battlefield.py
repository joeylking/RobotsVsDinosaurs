from fleet import Fleet
from herd import Herd
import random

# Gameplay: Welcome screen. Choose side. If robots, choose weapons. If dinosaurs, choose dinos? Begin battle. You pick your attacks, opponent attacks random?


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.display_welcome()

    def run_game(self):
        self.herd.create_herd()
        self.fleet.create_fleet()
        print("Let's battle!")
        self.battle()

    def display_welcome(self):
        print(100 * "*")
        print(100 * "*")
        print("Robots Vs Dinosaurs!")
        ready = input("Are you ready to play? [y/n] ")
        if ready == "y":
            print("Let's do this!")
            self.run_game()
        else:
            print("OK, bye!")

    def battle(self):
        print("Flipping a coint to determine who attacks first......")
        coin = random.randint(0,1)
        if coin == 0:
            print("Robots won the coin toss!")
            self.robo_turn()
        else:
            print("Dinosaurs won the toss!")
            self.dino_turn()


    def dino_turn(self):
        print("Dinosaurs' time to attack!")
        opponent = self.show_robo_opponent_options()
        dinosaur = input(f"Which dinosaur should attack?  1 - {self.herd.dinosaurs[0].name} 2 - {self.herd.dinosaurs[1].name} 3 - {self.herd.dinosaurs[2].name}  ")
        if dinosaur == "1":
            self.herd.dinosaurs[0].attack(opponent)
        elif dinosaur == "2":
            self.herd.dinosaurs[1].attack(opponent)
        if dinosaur == "3":
            self.herd.dinosaurs[2].attack(opponent)
        self.robo_turn()

    def robo_turn(self):
        print("Robots' time to attack!")
        opponent = self.show_dino_opponent_options()
        robot = input(f"Which robot should attack? 1 - {self.fleet.robots[0].name} 2 - {self.fleet.robots[1].name} 3 - {self.fleet.robots[2].name}")
        if robot == "1":
            self.fleet.robots[0].attack(opponent)
        elif robot == "2":
            self.fleet.robots[1].attack(opponent)
        elif robot == "3":
            self.fleet.robots[2].attack(opponent)
        self.dino_turn()

    def show_dino_opponent_options(self):
        opponent = input(f"Which dinosaur do you want to attack? 1 - {self.herd.dinosaurs[0].name} 2 - {self.herd.dinosaurs[1].name} 3 - {self.herd.dinosaurs[2].name} ")
        if opponent == "1":
            return self.herd.dinosaurs[0]
        elif opponent =="2":
            return self.herd.dinosaurs[1]
        elif opponent == "3":
            return self.herd.dinosaurs[2]

    def show_robo_opponent_options(self):
        opponent = input(f"Which robot do you want to attack? 1 - {self.fleet.robots[0].name} 2 - {self.fleet.robots[1].name} 3 - {self.fleet.robots[2].name} ")
        if opponent == "1":
            return self.fleet.robots[0]
        elif opponent == "2":
            return self.fleet.robots[1]
        elif opponent == "3":
            return self.fleet.robots[2]

    def display_winners(self):
        pass