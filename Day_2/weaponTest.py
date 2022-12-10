from weapon import Rock
from weapon import Weapon

assert Rock.allowsStrategy("A")

print (Weapon.fromStrategy("X"))

print (Weapon.fromStrategy("B").getScore())

print (Weapon.fromStrategy("Y").getResultAgainstWeapon(Weapon.fromStrategy("A")))

print (Weapon.fromStrategy("X").getResultAgainstWeapon(Weapon.fromStrategy("B")))

print (Weapon.fromStrategy("Z").getResultAgainstWeapon(Weapon.fromStrategy("C")))
