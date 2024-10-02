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

    def ucs(self, start, goal):
        frontier = [(0, start, [start])]  
        explored = set()

        while frontier:
            cost, current_node, path = heapq.heappop(frontier)
            if current_node == goal:
                return cost, path

            if current_node not in explored:
                explored.add(current_node)
                for neighbor, neighbor_cost in self.edges.get(current_node, []):
                    if neighbor not in explored:
                        heapq.heappush(frontier, (cost + neighbor_cost, neighbor, path + [neighbor]))

        return None, None 

edges = {
    'S': [('A', 2), ('B', 4)],
    'B': [('C', 2), ('G', 6)],
    'G': [],
    'A': [('B', 1), ('C', 4)],
    'C': [('G', 3)]
}

graph = Graph(edges)

start_node = 'S'
goal_node = 'G'
cost, path = graph.ucs(start_node, goal_node)

if cost is not None:
    print(f"Cost of the shortest path from {start_node} to {goal_node}: {cost}")
    print("Shortest path:", " -> ".join(path))
else:
    print("No path found")
