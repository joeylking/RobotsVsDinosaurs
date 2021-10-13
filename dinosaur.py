class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        print(f"{self.name} successfully attacked {robot.name}")
        robot.health = robot.health - self.attack_power
        print(f"{robot.name} has {str(robot.health)} health remaining.")