from herd import Herd
from fleet import Fleet

fleet = Fleet()
herd = Herd()

for dinosaur in herd.dinosaurs:
    print(dinosaur.name)

print(herd.herd_health)
print(fleet.fleet_health)

herd.dinosaurs[0].attack(fleet.robots[1])
fleet.robots[1].attack(herd.dinosaurs[1])
herd.calc_total_health(herd.dinosaurs)
fleet.calc_total_health(fleet.robots)

print(herd.herd_health)
print(fleet.fleet_health)