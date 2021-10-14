from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.fleet_health = 300

    def create_fleet(self):
        robot1_name = input("What is the name of your first robot?  ")
        robot1 = Robot(robot1_name)
        robot2_name = input("What is the name of your second robot?  ")
        robot2 = Robot(robot2_name)
        robot3_name = input("What is the name of your third robot?  ")
        robot3 = Robot(robot3_name)
        self.robots.extend([robot1, robot2, robot3])
        print("The robots are:")
        for robot in self.robots:
            print(robot.name)
    
    def calc_total_health(self, robos):
        health_values = []
        for robo in robos:
            health_values.append(robo.health)
            # print(f"{robo.name} health: {robo.health}")
        total = sum(health_values)
        print(f"Total fleet health: {total}")
        self.fleet_health = total

    