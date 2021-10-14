from weapon import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("default claw", 5, 0)

    def attack(self, dinosaur):
        hit = random.randint(0, 1)
        if hit == 0:
            print(50 * "!")
            print(f"{self.name}'s attack against {dinosaur.name} failed!")
        else:
            print(50 * "*")
            print(f"{self.name} successfully attacked {dinosaur.name} with a {self.weapon.name}")
            print(50 * "*")
            dinosaur.health = dinosaur.health - self.weapon.attack_power
            if dinosaur.health > 0:
                print(f"{dinosaur.name} has {dinosaur.health} health remaining.")
            else:
                print(50 * "-")
                print(f"{dinosaur.name} has been eliminated!")