from weapon import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = self.choose_weapon()

    def attack(self, dinosaur):
        hit = random.randint(0, 1)
        if hit == 0:
            print(f"{self.name}'s attack against {dinosaur.name} failed!")
        else:
            print(f"{self.name} successfully attacked {dinosaur.name} with a {self.weapon.name}")
            dinosaur.health = dinosaur.health - self.weapon.attack_power
        print(f"{dinosaur.name} has {dinosaur.health} health remaining.")

    def choose_weapon(self):
        bat = Weapon("really big bat", 10)
        chainsaw = Weapon("chainsaw", 20)
        laser = Weapon("laser", 30)
        print(f"Choose {self.name}'s weapon: ")
        choice = input("1 - bat  2 - chainsaw  3 - laser  ")
        if choice == "1":
            print(f"Excellent. {self.name} now has a {bat.name}")
            return bat
        elif choice == "2":
            print(f"Excellent. {self.name} now has a {chainsaw.name}")
            return chainsaw
        elif choice == "3":
            print(f"Excellent. {self.name} now has a {laser.name}")
            return laser
