from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
        
    def create_herd(self):
        t_rex = Dinosaur("T-Rex", 30)
        triceratops = Dinosaur("Triceratops", 20)
        raptor = Dinosaur("Raptor", 10)
        self.dinosaurs.extend([t_rex, triceratops, raptor])