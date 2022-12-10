from pathlib import Path
from weapon import Weapon
from expectedResultType import ExpectedResultType

path = Path(__file__).with_name('input.txt')
with path.open() as file:
    total_score = 0
    for line in file:
        strippedLine = line.strip()
        
        opponent_weapon = Weapon.fromStrategy(strippedLine[0])
        my_weapon = Weapon.fromStrategy(strippedLine[2])

        fight_result = my_weapon.fight(opponent_weapon)
        
        total_score += fight_result
    print(f"Part1 :: Total strategy score: {total_score}")


with path.open() as file:
    total_score = 0
    for line in file:
        strippedLine = line.strip()
        
        opponent_weapon = Weapon.fromStrategy(strippedLine[0])
        opponent_expected_result = ExpectedResultType.from_value(strippedLine[2])
        my_weapon = opponent_weapon.getWeaponTo(opponent_expected_result)

        fight_result = my_weapon.fight(opponent_weapon)
        
        total_score += fight_result
    print(f"Part2 :: Total strategy score: {total_score}")


