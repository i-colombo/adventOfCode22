from dijkstra import Graph

def minimumDistancesTo(height_map: list, start_index: int) -> list:
    vertices_num = len(height_map) * len(height_map[0])
    g = Graph(vertices_num)
    g.graph = adjacencyMapFromHeightMap(height_map)
    return g.dijkstra(start_index)

def adjacencyMapFromHeightMap(height_map: list) -> list:
    vertices_count = len(height_map) * len(height_map[0])
    adjacency_map = []
    for i, map_line in enumerate(height_map):
        vertices_line_num = len(map_line)
        for j, current_map_height in enumerate(map_line):
            vertex_connections = [0] * vertices_count
            if i > 0:
                connection_height = height_map[i-1][j]
                computeVertexConnection(current_map_height, connection_height, vertex_connections, i-1, j, vertices_line_num)
            if j > 0:
                connection_height = height_map[i][j-1]
                computeVertexConnection(current_map_height, connection_height, vertex_connections, i, j-1, vertices_line_num)
            if i < len(height_map) - 1:
                connection_height = height_map[i+1][j]
                computeVertexConnection(current_map_height, connection_height, vertex_connections, i+1, j, vertices_line_num)
            if j < len(map_line) - 1:
                connection_height = height_map[i][j+1]
                computeVertexConnection(current_map_height, connection_height, vertex_connections, i, j+1, vertices_line_num)
            adjacency_map.append(vertex_connections)
    return adjacency_map


def computeVertexConnection(current_height, connection_height, connections, connection_i, connection_j, map_width):
    if connection_height - current_height <= 1:
        connection_adjacency_index = connection_i * map_width + connection_j
        connections[connection_adjacency_index] = 1
