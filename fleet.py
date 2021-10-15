from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.fleet_health = 300
        self.weapons = []
        self.create_weapons()

    def create_fleet(self):
        robot1_name = input("What is the name of your first robot?  ")
        robot1 = Robot(robot1_name)
        self.choose_weapon(robot1)
        robot2_name = input("What is the name of your second robot?  ")
        robot2 = Robot(robot2_name)
        self.choose_weapon(robot2)
        robot3_name = input("What is the name of your third robot?  ")
        robot3 = Robot(robot3_name)
        self.choose_weapon(robot3)
        self.robots.extend([robot1, robot2, robot3])
        print( 50 * "-")
        print("The Robots are:")
        for robot in self.robots:
            print(robot.name)
        print( 50 * "-")

    def create_weapons(self):
        bat = Weapon("really big bat", 10, 1)
        chainsaw = Weapon("chainsaw", 20, 2)
        laser = Weapon("laser", 30, 3)
        self.weapons.extend([bat, chainsaw, laser])
    
    def calc_total_health(self, robos):
        health_values = []
        for robo in robos:
            health_values.append(robo.health)
            # print(f"{robo.name} health: {robo.health}")
        total = sum(health_values)
        print(f"Total fleet health: {total}")
        self.fleet_health = total

    def choose_weapon(self, robot):
            print(f"Choose {robot.name}'s weapon: ")
            for weapon in self.weapons:
                print(f"{weapon.key} - {weapon.name}")
            choice = int(input(""))
            for weapon in self.weapons:
                if weapon.key == choice:
                    self.weapons.remove(weapon)
                    robot.weapon = weapon