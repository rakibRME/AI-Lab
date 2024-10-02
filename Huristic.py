import heapq

class Graph:
    def __init__(self, edges=None):
        self.edges = {}
        if edges:
            self.add_edges(edges)

    def add_edges(self, edges):
        for start, end_costs in edges.items():
            for end, cost in end_costs:
                self.add_edge(start, end, cost)

    def add_edge(self, start, end, cost):
        self.edges.setdefault(start, []).append((end, cost))

    def astar_search(self, start, goal, heuristic):
        frontier = [(0 + heuristic(start), start, [])]  # (f-value, node, path)
        explored = set()

        while frontier:
            f, current_node, path = heapq.heappop(frontier)
            if current_node == goal:
                return path + [current_node]

            if current_node not in explored:
                explored.add(current_node)
                for neighbor, neighbor_cost in self.edges.get(current_node, []):
                    if neighbor not in explored:
                        g = len(path) + 1  # Cost from start to current node (path length)
                        h = heuristic(neighbor)  # Heuristic value for the neighbor
                        heapq.heappush(frontier, (g + h, neighbor, path + [current_node]))

        return None  # No path found

# Example usage
edges = {
    'S': [('A', 2), ('B', 4)],
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('G', 6)],
    'C': [('G', 3)],
    'G': []
}

graph = Graph(edges)

def h1(node):
    heuristic_values = {'S': 7, 'A': 5, 'B': 5, 'C': 3, 'G': 0}
    return heuristic_values[node]

start_node = 'S'
goal_node = 'G'

path = graph.astar_search(start_node, goal_node, h1)

if path:
    print("Shortest path:", " -> ".join(path))
else:
    print("No path found")
