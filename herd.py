from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.herd_health = 300

    def create_herd(self):
        t_rex = Dinosaur("T-Rex", 30)
        triceratops = Dinosaur("Triceratops", 20)
        raptor = Dinosaur("Raptor", 10)
        self.dinosaurs.extend([t_rex, triceratops, raptor])
        print("The dinosaurs are:")
        for dinosaur in self.dinosaurs:
            print(dinosaur.name)

    def calc_total_health(self, dinos):
        health_values = []
        for dino in dinos:
            health_values.append(dino.health)
            print(f"{dino.name} health: {dino.health}")
        total = sum(health_values)
        print(f"Total herd health: {total}")
        self.herd_health = total