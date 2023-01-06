class Node():
    def __init__(self, height: str, related_nodes: list) -> None:
        self.name = height
        
        self.is_starting_node = False
        self.is_finishing_node = False

        if height == 'S':
            self.weight = 0
            self.is_starting_node = True
        elif height == 'E':
            self.weight = ord("z") - 97
            self.is_finishing_node = True
        else:
            self.weight = ord(height) - 97
        
        self.nodes = set()
        for related_node in related_nodes:
            if related_node != None:
                self.addNode(related_node)
                related_node.addNode(self)

    def __repr__(self):
        return f'Name: {self.name} - Weight: {self.weight} - Related Nodes: {[node.weight for node in self.nodes]} - Starting: {self.is_starting_node} - Finishing: {self.is_finishing_node}'
    
    def addNode(self, node: 'Node'):
        if (node.weight - self.weight) in [0, 1]:
            self.nodes.add(node)

    def minimumStepsToFinish(self, visited_nodes: set) -> int:
        if self.is_finishing_node:
            return 0
        if any(node.is_finishing_node for node in self.nodes):
            return 1
                
        steps_from_nodes = self.stepsFromChildNodes(visited_nodes.copy())    
        
        if len(steps_from_nodes) == 0:
            return None
        else:
            return min(steps_from_nodes) + 1

    def stepsFromChildNodes(self, visited_nodes: set) -> list:    
        visited_nodes.add(self)
        unvisited_nodes = self.nodes - visited_nodes
        steps_from_nodes = []
        
        for node in unvisited_nodes:
            steps = node.minimumStepsToFinish(visited_nodes)
            if steps != None:
                steps_from_nodes.append(steps)
        
        return steps_from_nodes
