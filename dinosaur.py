import random

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        hit = random.randint(0,1)
        if hit == 0:
            print(50 * "!")
            print(f"{self.name}'s attack against {robot.name} was unsuccessful!")
        else:
            print(50 * "*")
            print(f"{self.name} successfully attacked {robot.name}")
            print(50 * "*")
            robot.health = robot.health - self.attack_power
            if robot.health > 0 :
                print(f"{robot.name} has {robot.health} health remaining.")
            else:
                print(50 * "-")
                print(f"{robot.name} has been eliminated!")
