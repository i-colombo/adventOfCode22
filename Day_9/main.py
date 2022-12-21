from pathlib import Path
from cartesian import *

path = Path(__file__).with_name('input.txt')
head = (0, 0)
tail = (0, 0)
tail_position_history = {tail}

with path.open() as file:
    for line in file:
        movement = line.strip().split(" ")
        for _ in range(int(movement[1])):
            previous_head_position = head
            head = move(head, movement[0])
            
            if not areTouching(head, tail):
                tail = previous_head_position
                tail_position_history.add(tail)

print(f"Part 1 :: Tail positions: {tail_position_history} :: Positions count: {len(tail_position_history)}")

######################  PART 2 ###################################
rope = []
for _ in range(10):
    rope.append((5,12))
head = rope[0]
tail_position_history = {(0,0)}

with path.open() as file:
    for line in file:
        movement = line.strip().split(" ")
        for _ in range(int(movement[1])):
            head = move(head, movement[0])
            rope[0] = head
            
            for i in range(1, len(rope)):
                previous_knot = rope[i-1]
                current_knot = rope[i]
                if not areTouching(previous_knot, current_knot):
                    current_knot = moveCloserTo(current_knot, previous_knot)
                    rope[i] = current_knot
                    if i == len(rope) -1:
                        tail_position_history.add(current_knot)

print(f"Part 2 :: Tail positions: {tail_position_history} :: Positions count: {len(tail_position_history)}")
