# class Graph:
#     def __init__(self, n):
#         self.adj = {}
#         self.visited = [False] * (n + 1)

#     def add_edge(self, u, v):
#         if u not in self.adj:
#             self.adj[u] = []
#         self.adj[u].append(v)
#         #self.adj[v].append(u)

#     def dfs(self, u):
#         self.visited[u] = True
#         print(u, end=" ")
#         if u in self.adj:
#             for v in self.adj[u]:
#                 if not self.visited[v]:
#                     self.dfs(v)

# n = int(input("Enter node number: "))
# graph = Graph(n)
# for _ in range(int(input("Enter edge number: "))):
#     u, v = map(int, input("Enter nodes connected by an edge (space-separated): ").split())
#     graph.add_edge(u, v)

# start_node = int(input("Enter starting node for DFS: "))
# graph.dfs(start_node)




from collections import deque
class Graph:
    def __init__(self, n):
        self.adj = {}
        self.visited = [False] * (n + 1)

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
  

    def bfs(self, start):
        queue = deque([start])
        self.visited[start] = True

        while queue:
            u = queue.popleft()
            print(u, end=" ")

            if u in self.adj:
                for v in self.adj[u]:
                    if not self.visited[v]:
                        queue.append(v)
                        self.visited[v] = True

n = int(input("Enter node number: "))
graph = Graph(n)
for _ in range(int(input("Enter edge number: "))):
    u, v = map(int, input("Enter nodes connected by an edge (space-separated): ").split())
    graph.add_edge(u, v)

start_node = int(input("Enter starting node for BFS: "))
graph.bfs(start_node)



# from collections import deque

# # Function to perform Breadth First Search on a graph
# # represented using adjacency list
# def bfs(adjList, startNode, visited):
#     # Create a queue for BFS
#     q = deque()

#     # Mark the current node as visited and enqueue it
#     visited[startNode] = True
#     q.append(startNode)

#     # Iterate over the queue
#     while q:
#         # Dequeue a vertex from queue and print it
#         currentNode = q.popleft()
#         print(currentNode, end=" ")

#         # Get all adjacent vertices of the dequeued vertex
#         # If an adjacent has not been visited, then mark it visited and enqueue it
#         for neighbor in adjList[currentNode]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 q.append(neighbor)

# # Function to add an edge to the graph
# def addEdge(adjList, u, v):
#     adjList[u].append(v)

# def main():
#     # Number of vertices in the graph
#     vertices = 5

#     # Adjacency list representation of the graph
#     adjList = [[] for _ in range(vertices)]

#     # Add edges to the graph
#     addEdge(adjList, 0, 1)
#     addEdge(adjList, 0, 2)
#     addEdge(adjList, 1, 3)
#     addEdge(adjList, 1, 4)
#     addEdge(adjList, 2, 4)

#     # Mark all the vertices as not visited
#     visited = [False] * vertices

#     # Perform BFS traversal starting from vertex 0
#     print("Breadth First Traversal starting from vertex 0:", end=" ")
#     bfs(adjList, 0, visited)

# if __name__ == "__main__":
#     main()