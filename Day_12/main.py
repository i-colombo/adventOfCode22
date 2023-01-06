from pathlib import Path
from graphs import Node

path = Path(__file__).with_name('testInput.txt')
map = []
with path.open() as file:
    map = [line.strip() for line in file.readlines()]

nodes_map = []
starting_node = None
for i, map_line in enumerate(map):
    nodes_map.insert(i, [])
    for j, map_item in enumerate(map_line):
        related_nodes = []
        if i > 0:
            related_nodes.append(nodes_map[i-1][j])
        if j > 0:
            related_nodes.append(nodes_map[i][j-1])
        node = Node(map_item, related_nodes)
        nodes_map[i].append(node)
        if map_item == "S":
            starting_node = node

print(starting_node.minimumStepsToFinish(set()))

