from dijkstra import Graph

def minimumDistancesStartingFrom(adjacency_map: list, start_index: int) -> list:
    vertices_num = len(adjacency_map)
    g = Graph(vertices_num)
    g.graph = adjacency_map
    return g.dijkstra(start_index)

def adjacencyMapFromHeightMap(height_map: list, calculateConnectionWeight: 'function') -> list:
    vertices_count = len(height_map) * len(height_map[0])
    adjacency_map = []
    for i, map_line in enumerate(height_map):
        vertices_line_num = len(map_line)
        for j, current_map_height in enumerate(map_line):
            vertex_connections = [0] * vertices_count
            if i > 0:
                connection_height = height_map[i-1][j]
                connection_adjacency_index = (i-1) * vertices_line_num + j
                vertex_connections[connection_adjacency_index] = calculateConnectionWeight(current_map_height, connection_height)
            if j > 0:
                connection_height = height_map[i][j-1]
                connection_adjacency_index = i * vertices_line_num + j-1
                vertex_connections[connection_adjacency_index] = calculateConnectionWeight(current_map_height, connection_height)
            if i < len(height_map) - 1:
                connection_height = height_map[i+1][j]
                connection_adjacency_index = (i + 1) * vertices_line_num + j
                vertex_connections[connection_adjacency_index] = calculateConnectionWeight(current_map_height, connection_height)
            if j < len(map_line) - 1:
                connection_height = height_map[i][j+1]
                connection_adjacency_index = i * vertices_line_num + j+1
                vertex_connections[connection_adjacency_index] = calculateConnectionWeight(current_map_height, connection_height)
            adjacency_map.append(vertex_connections)
    return adjacency_map
