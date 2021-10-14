import random

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        hit = random.randint(0,1)
        if hit == 0:
            print(f"{self.name}'s attack against {robot.name} was unsuccessful!")
        else:
            print(f"{self.name} successfully attacked {robot.name}")
            robot.health = robot.health - self.attack_power
        print(f"{robot.name} has {robot.health} health remaining.")
