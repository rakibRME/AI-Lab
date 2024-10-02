
# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
#         if(u == v):
#             print(f"Self loop in node {u}")
            
#     def BFS(self, s):

#         visited = [False] * (max(self.graph) + 1)
#         queue = []
#         queue.append(s)
#         visited[s] = True

#         while queue:
#             s = queue.pop(0)
#             print(s, end=" ")
#             for i in self.graph[s]:
#                 if visited[i] == False:
#                     queue.append(i)
#                     visited[i] = True
# graph = Graph()
# graph.addEdge(0, 1)
# graph.addEdge(1, 5)
# graph.addEdge(5, 2)
# graph.addEdge(2, 4)
# graph.addEdge(4, 6)
# graph.addEdge(6, 1)
# graph.addEdge(4, 3)
# graph.addEdge(3, 2)
# graph.addEdge(3, 1)
# graph.addEdge(3, 0)
# graph.addEdge(1, 2)

# graph.BFS(0)


from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        if u == v:
            print(f"Self loop in node {u}")

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * (max(self.graph) + 1)
        self.DFSUtil(v, visited)


graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(1, 5)
graph.addEdge(5, 2)
graph.addEdge(2, 4)
graph.addEdge(4, 6)
graph.addEdge(6, 1)
graph.addEdge(4, 3)
graph.addEdge(3, 2)
graph.addEdge(3, 1)
graph.addEdge(3, 0)
graph.addEdge(1, 2)

graph.DFS(0)
