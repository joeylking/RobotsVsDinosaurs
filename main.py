from herd import Herd
from fleet import Fleet

fleet = Fleet()
herd = Herd()

for dinosaur in herd.dinosaurs:
    print(dinosaur.name)

herd.dinosaurs[0].attack(fleet.robots[0])