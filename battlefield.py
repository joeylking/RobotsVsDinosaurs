from fleet import Fleet
from herd import Herd
import random
import text_art

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
        text_art.welcome_art()
        ready = input("Are you ready to play? [y/n] ")
        if ready == "y":
            print("Let's do this!")
            self.run_game()
        else:
            print("OK, bye!")

    def battle(self):
        input("Enter anything to flip a coin to determine which team attacks first: ")
        print("Flipping the coin......")
        print( 50 * ".")
        print( 50 * ".")
        print( 50 * ".")
        coin = random.randint(0,1)
        if coin == 0:
            print("Robots won the coin toss!")
            self.robo_turn()
        else:
            print("Dinosaurs won the toss!")
            self.dino_turn()


    def dino_turn(self):
        text_art.dino_attack()
        print("Dinosaurs' time to attack!")
        opponent = self.show_dino_opponent_options()
        print("Who should lead the attack?")
        for dino in self.herd.dinosaurs:
            print(f"{self.herd.dinosaurs.index(dino) + 1} - {dino.name}")
        i = int(input()) - 1
        attacker = self.herd.dinosaurs[i]
        attacker.attack(opponent)
        if opponent.health <= 0:
            self.fleet.robots.remove(opponent)
        if len(self.fleet.robots) > 0:
            self.fleet.calc_total_health(self.fleet.robots)
            self.robo_turn()
        else:
            self.display_winners(self.herd.dinosaurs, "Dinosaurs")

    def robo_turn(self):
        text_art.robot_attack()
        print("Robots' time to attack!")
        opponent = self.show_robo_opponent_options()
        print(f"Who should lead the attack?")
        for robo in self.fleet.robots:
            print(f"{self.fleet.robots.index(robo) + 1} - {robo.name}")
        i = int(input()) - 1
        attacker = self.fleet.robots[i]
        attacker.attack(opponent)
        if opponent.health <= 0:
            self.herd.dinosaurs.remove(opponent)
        if len(self.herd.dinosaurs) > 0:
            self.herd.calc_total_health(self.herd.dinosaurs)
            self.dino_turn()
        else:
            self.display_winners(self.fleet.robots, "Robots")

    def show_dino_opponent_options(self):
        print("Choose the target of your attack:")
        for robo in self.fleet.robots:
            print(f"{self.fleet.robots.index(robo) + 1} - {robo.name}")
        i = int(input()) - 1
        opponent = self.fleet.robots[i]
        return opponent

    def show_robo_opponent_options(self):
        print("Choose the target of your attack:")
        for dino in self.herd.dinosaurs:
            print(f"{self.herd.dinosaurs.index(dino) + 1} - {dino.name}")
        i = int(input()) - 1
        opponent = self.herd.dinosaurs[i]
        return opponent

    def display_winners(self, winners, team):
        text_art.winner(team)
        print(f"Congrats to team {team}! You won!")
        print("Last player(s) standing: ")
        for winner in winners:
            print(f"{winner.name}")