from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = self.choose_weapon()      # Weapon("claw", 5)

    def attack(self, dinosaur):
        pass

    def choose_weapon(self):
        bat = Weapon("really big bat", 10)
        chainsaw = Weapon("chainsaw", 20)
        laser = Weapon("laser", 30)
        print(f"Choose {self.name}'s weapon:")
        choice = input("1 - bat  2 - chainsaw  3 - laser  ")
        if choice == "1":
            print(f"Excellent. {self.name} how has a {bat.name}")
            return bat
        elif choice == "2":
            print(f"Excellent. {self.name} how has a {chainsaw.name}")
            return chainsaw
        elif choice == "3":
            print(f"Excellent. {self.name} how has a {laser.name}")
            return laser
