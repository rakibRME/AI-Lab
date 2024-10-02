from collections import deque

def bfs_traversal(n, adjacency_list):
    visited = [False] * n
    bfs_result = []
    queue = deque([0])  # Start BFS from node 0
    visited[0] = True
    
    while queue:
        node = queue.popleft()
        bfs_result.append(node)
        
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                
    return bfs_result

def main():
    # Read input from a file
    with open('input.txt', 'r') as file:
        data = file.read().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        adjacency_list = []
        
        for i in range(n):
            m = int(data[index])
            index += 1
            if m > 0:
                adjacency_list.append(list(map(int, data[index:index + m])))
                index += m
            else:
                adjacency_list.append([])
        
        result = bfs_traversal(n, adjacency_list)
        results.append(result)
    
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__": 
    main()
