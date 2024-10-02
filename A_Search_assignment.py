def Reheap_up(queue):
    index = len(queue)-1
    while index > 0:
        parent_index = (index - 1) // 2
        if queue[index][0] < queue[parent_index][0]:
            queue[index], queue[parent_index] = queue[parent_index], queue[index]
            index = parent_index
        else:
            break

def Reheap_down(queue):
    n = len(queue)
    parent = 0
    while True:
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2
        min = parent
        if left_child < n and queue[left_child][0] < queue[min][0]:
            min = left_child
        if right_child < n and queue[right_child][0] < queue[min][0]:
            min = right_child

        if min != parent:
            queue[parent], queue[min] = queue[min], queue[parent]
            parent = min
        else:
            break


def enqueue(queue, i):
    queue.append(i)
    Reheap_up(queue)

def dequeue(queue):
    x = queue.pop(0)
    Reheap_down(queue)
    return x


def UCS(graph, start, goal, heuristic_cost):
    visited = []
    flag = False
    queue = [(0 + heuristic_cost[start], start, [start])]  

    while queue:
        cost, node, path = dequeue(queue)
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            flag = True
            break

        for i, i_cost in graph[node].items():
            if i not in visited:
                new_cost = cost - heuristic_cost[node] + i_cost + heuristic_cost[i]  
                new_path = path + [i]
                enqueue(queue, (new_cost, i, new_path))

    if flag == True:
        print(path)
        print("Total Cost ")
        print(cost)

graph = {
        'S': {'A': 2, 'B': 4},
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'G': 6},
        'C': {'G': 3},
        'G': {}
}

h1= {'S' : 8,'A' : 3,'B' : 7,'C' : 2,'G' : 0}
h2 = {'S' : 7,'A' : 4,'B' : 5,'C' : 2,'G' : 0}
h3 = {'S' : 7,'A' : 5,'B' : 5,'C' : 3,'G' : 0}

print("\nPath list for h1")        
UCS(graph, "S", "G", h1)
print("\nPath list for h2")    
UCS(graph, "S", "G", h2)
print("\nPath list for h3")    
UCS(graph, "S", "G", h3)
